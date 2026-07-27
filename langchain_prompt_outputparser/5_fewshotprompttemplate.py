from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples=[
        {"input": "高兴", "output": "愉悦"},
        {"input": "快速", "output": "迅猛"},
        {"input": "美丽", "output": "绚丽"}
    ]

example_prompt=PromptTemplate.from_template("{input} 的同义词是 {output}")

few_shot_template=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="请根据以下示例，将输入词语转换为同义词",
    suffix="基于示例回答问题。用户输入：{input}\n输出：",
    input_variables=["input"]

)
prompt_text=few_shot_template.format(input="高兴")  #.format 关键字传入
print(type(few_shot_template))
print(few_shot_template)
print(prompt_text)
print(type(prompt_text))

llm=Tongyi(model='qwen-max')
result=llm.invoke(prompt_text)
print(result)