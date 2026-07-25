from langchain_community.llms.tongyi import Tongyi

llm=Tongyi(model='qwen-max')
result=llm.stream('你是谁')  # 流式输出
for chunk in result:
    print(chunk,end='', flush=True)