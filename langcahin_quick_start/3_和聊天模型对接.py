from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

llm=ChatTongyi(model='qwen3-max')

chat_history=[
    SystemMessage(content='你是谁'),
    HumanMessage(content='你是谁')
]

result=llm.invoke(input=chat_history)
print(type(result))
print(result)