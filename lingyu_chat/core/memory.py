from typing import Dict, List
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage

from .chat_history_manager import ChatHistoryManager
from .summary_manager import SummaryManager
from .facts_manager import FactManager

# 会话Key前缀
SESSION_KEY = "session"


class Memory:
    """记忆管理整合类：组合三个独立管理器"""

    def __init__(self, chat_session_id: str) -> None:
        self.chat_session_id = chat_session_id
        self.session_key = f"{SESSION_KEY}:{chat_session_id}"
        # 初始化三个子管理器
        self.history = ChatHistoryManager(self.session_key)
        self.summary = SummaryManager(self.session_key)
        self.facts = FactManager(self.session_key)

    # ========== 对话历史相关（委托） ==========
    def get_session_history(self):
        return self.history.get_history()

    def get_messages(self) -> List[BaseMessage]:
        return self.history.get_messages()

    def get_recent_messages(self, recent_n: int) -> List[BaseMessage]:
        """获取最近 N 条消息"""
        return self.history.get_recent_messages(recent_n)

    # 获取上下文
    def get_recent_messages_text(self, recent_n: int) -> str:
        messages = self.get_recent_messages(recent_n)
        messages_text = ""
        for msg in messages:
            if isinstance(msg, HumanMessage):
                messages_text += f"human:{msg.content}\n"
            elif isinstance(msg, AIMessage):
                messages_text += f"ai:{msg.content}\n"
        return messages_text

    # ========== 添加消息（触发摘要逻辑） ==========
    def add_user_message(self, message: str, llm=None) -> None:
        self.history.add_user_message(message)
        self.summary.increment_unsummarized_count(1)
        # 判断是否需要触发摘要更新
        self._trim_and_summarized(llm)

    def add_ai_message(self, message: str, llm=None) -> None:
        """添加AI消息并触发摘要检查"""
        self.history.add_ai_message(message)
        self.summary.increment_unsummarized_count(1)
        # 判断是否需要触发摘要更新
        self._trim_and_summarized(llm)

    # ========== 关键事实相关（委托） ==========
    def get_key_facts(self) -> Dict[str, str]:
        return self.facts.get_all_facts()

    def update_key_facts(self, facts: Dict[str, str]) -> None:
        self.facts.update_facts(facts)

    def clear_key_facts(self) -> None:
        self.facts.clear_facts()

    # ========== 摘要相关（委托） ==========
    def _trim_and_summarized(self, llm=None) -> None:
        if not self.summary.should_trigger_summary():
            return

        history = self.history.get_history()
        if not history:
            return

        messages = self.get_messages()  # 获取所有消息
        unsummarized_count = self.summary.get_unsummarized_count()  # 获取未摘要消息数量
        total_count = len(messages)  # 获取消息总数
        summarized_count = total_count - unsummarized_count  # 已摘要消息数量

        # 获取未摘要的消息
        new_messages = messages[summarized_count:]
        if new_messages:
            old_summary = self.summary.get_summary()
            new_summary = self.summary.generate_incremental_summary(
                old_summary,
                new_messages,
                llm
            )
            self.summary.update_summary(new_summary)
            self.summary.reset_unsummarized_count()
            print("摘要生成")

    # ========== 准备LLM上下文 ==========
    def prepare_memory_for_llm(self) -> List[BaseMessage]:
        """准备传递给LLM的上下文（事实 + 摘要 + 最近消息）"""
        result = []

        # 1. 添加关键事实
        facts = self.facts.get_all_facts()  # 获取关键事实
        if facts:
            facts_text = " | ".join([f"{k}:{v}" for k, v in facts.items()])
            result.append(AIMessage(content=f"[关键事实] {facts_text}"))
        # 2. 添加摘要
        summary = self.summary.get_summary()  # 获取摘要
        if summary:
            result.append(AIMessage(content=f"[摘要] {summary}"))
        # 3. 添加最近未摘要的消息
        unsummarized_count  = self.summary.get_unsummarized_count()
        if unsummarized_count > 0:
            messages = self.history.get_messages()  # 获取所有消息
            recent_messages = messages[-unsummarized_count:]  # 列表切片：取最后 N 条未摘要消息

           # extend(可迭代对象)：把列表 / 元组 / 生成器拆成一个个零散元素再加进去
           #  加单条消息对象：result.append(AIMessage(...))（前面添加关键事实那行就是用
           #  append）
           #  加一整批多条消息列表：result.extend(消息列表)（当前这段代码）
            result.extend(recent_messages)

        return result