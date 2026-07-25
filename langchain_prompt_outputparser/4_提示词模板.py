from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate


prompt_template=PromptTemplate.from_template(
    "假设你是一个{expert}专家,请你解释一下什么是{content}"
)

# 创建模型客户端
llm=Tongyi(model='qwen-max')

# 组成LCEL表达式
chain=prompt_template | llm

# 流式输出
result1=chain.stream({'expert':'机器学习','content':'机器学习'})
print(type(result1))
# for循环生成器
for chunk in result1:
    print(chunk,end='', flush=True)


# .invoke 传入字典
# result=chain.invoke({'expert':'机器学习','content':'机器学习'})
# print(result)

# .format 传入关键字参数
# result=llm.invoke(prompt_template.format(exper='机器学习',content='机器学习'))



