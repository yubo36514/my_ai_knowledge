from typing import Dict, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

_session_store: Dict[str, BaseChatMessageHistory] = {}


class Memory:
    # 获取回话历史记录
    def get_session_history(self, chat_session_id: str) -> BaseChatMessageHistory:
        if chat_session_id not in _session_store:
            _session_store[chat_session_id] = InMemoryChatMessageHistory()
        return _session_store[chat_session_id]

    # 添加人类消息
    def add_human_message(self, chat_session_id: str, message: str | HumanMessage) -> None:
        chat_history = self.get_session_history(chat_session_id)
        if isinstance(message, str):
            chat_history.add_message(HumanMessage(message))
        else:
            chat_history.add_message(message)

    # 添加ai回复消息
    def add_ai_message(self, chat_session_id: str, message: str | AIMessage)-> None:
        chat_history=self.get_session_history(chat_session_id)
        if isinstance(message, str):
            chat_history.add_message(AIMessage(message))
        else:
            chat_history.add_message(message)

    def messages(self, chat_session_id: str) -> List[BaseMessage]:
        return self.get_session_history(chat_session_id).messages


class ChatSession:
    def __init__(self, session_id: str, system_prompt: str = "你是小美"):
        # 1. 把外部传入的参数绑定为实例属性（最基础操作）
        self.session_id = session_id

        # 2. 依赖类实例化（组合模式，把别的类装进来）
        self.memory = Memory()  # 会话记忆管理器

        # 3. 底层大模型客户端初始化
        self.model = ChatTongyi(model="qwen3-max", streaming=True)

        # 4. 固定业务模板/规则初始化
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")

        ])  # 提示词模板
        self.parser = StrOutputParser()  # 输出解析器

        # 5. 直接组装固定链路（LangChain 管道）
        self.chain = self.prompt | self.model | self.parser

    def send(self, content: str):
        chat_history=self.memory.messages(self.session_id)
        stream=self.chain.stream(input={
            "chat_history": chat_history,
            "input": content
        })
        full_reply=""
        for chunk in stream:
            full_reply+=chunk
            print(chunk, end="", flush=True)
            yield chunk
        self.memory.add_human_message(self.session_id, content)
        self.memory.add_ai_message(self.session_id, full_reply)


if __name__ == '__main__':
    # system_prompt = """
    # 你的回答要求：
    # 1. 语言流畅通顺，禁止重复字词、重复半句、重复整句话；
    # 2. 不要括号嵌套多余情绪标注，如需动作描写简洁一句话带过即可；
    # 3. 分段自然，口语自然连贯，不要卡顿式折返表述；
    # 4. 回应简短自然，不要过度堆砌碎碎念。
    # 身份：温柔活泼的陪伴型助手小丽
    # """
    chat_session = ChatSession(session_id="1")

    while True:
        content = input("用户：")
        if content.strip() in ["exit", "quit"]:
            print("对话结束")
            break
        else:
            if not content.strip():
                print("请勿输入空白内容")
                continue
        print("AI：", end="", flush=True)
        for chunk in chat_session.send(content):
            print(chunk, end="", flush=True)
        print()
        print("="*50)
