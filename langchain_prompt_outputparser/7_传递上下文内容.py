from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#
# user_input = input('用户：')
#
# chat_prompt_template = ChatPromptTemplate.from_messages([
#     ("system", "假设你是一个AI专家"),
#     MessagesPlaceholder("history"),
#     ("human", "{user_input}"),
# ])
#
# chat_history = [
#     ("human", "什么是Langgraph"),
#     ("ai", "LangGraph是一种将自然语言处理（NLP）与图神经网络（GNN, Graph Neural Networks）相结合的技术或方法。")
# ]
#
#
#
# # print(chat_prompt_template.invoke(input={"history": chat_history}))
# llm = ChatTongyi(model="qwen3-max")
# chain = chat_prompt_template | llm
# result = chain.stream(input={"history": chat_history, "user_input": user_input})
# for chunk in result:
#     print(chunk.content, end="", flush=True)
#
# # print(type(result)) # <class 'langchain_core.messages.ai.AIMessage'>
# # print(result) # content='你刚才问的是：“什么是Langgraph”。' additional_kwargs={} res
# # print(result.content) # 你刚才问的是：“什么是Langgraph”。


class MutiTurnChat():
    def __init__(self, model, system_prompt,streaming=True):
        self.llm=ChatTongyi(model=model, streaming=streaming)
        self.chat_history=[]
        if system_prompt:
            self.chat_history.append(('system',system_prompt))

        self.prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="history"),
            ("human", "{user_input}")
        ])
        # 拼接 LCEL 执行链
        self.chain = self.prompt | self.llm

    def add_user_message(self, content):
        self.chat_history.append(('user',content))

    def add_ai_message(self, content):
        self.chat_history.append(('ai',content))

    def send(self):

        full_reply=''
        result=self.chain.stream(input={"history": self.chat_history, "user_input": user_input})
        for chunk in result:
            print(chunk.content,end='', flush=True)
            full_reply+=chunk.content
        print()
        self.add_ai_message(full_reply)


if __name__ == '__main__':
    model='qwen3-max'
    system_prompt='你是一个非常出色的ai教学老师'
    chat=MutiTurnChat(model,system_prompt)
    while True:
        user_input=input('用户：')
        if user_input.strip() in ['exit', 'quit']:
            print('对话结束')
            break
        if not user_input.strip():
            print('请勿输入空白内容')
            continue
        chat.add_user_message(user_input)
        chat.send()
