from langchain_community.llms.tongyi import Tongyi

llm=Tongyi(model='qwen-max')

result=llm.invoke('你是谁')  # 一次性输出
print(type(result))
print(result)
