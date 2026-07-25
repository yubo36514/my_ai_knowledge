from langchain_community.chat_models import ChatTongyi

llm=ChatTongyi(model='qwen3-max', streaming=True)

chat_history=[
    # SystemMessage(content='你是谁'),
    # HumanMessage(content='你是谁')
    # ('system','你是一个出色的ai老师'),
    # ('human','你是谁')
]

result=llm.stream(input=chat_history)
print(result)

for chunk in result:
    # print(chunk)
    print(chunk.content,end='', flush=True)
