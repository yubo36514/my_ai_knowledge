from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.prompt_values import StringPromptValue, ChatPromptValue

# ===================== 1. 第一种：PromptValue 对象（分为两种子类） =====================
# 1.1 StringPromptValue 普通文本PromptValue
str_prompt_template = PromptTemplate.from_template("你好，{name}")
prompt_value_1 = str_prompt_template.invoke(input={"name": "小明"})

# 1.2 ChatPromptValue 对话类型PromptValue
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("human", "你好呀")
])
prompt_value_2 = chat_prompt_template.invoke({})

print("===== 1. PromptValue 类型 =====")
print(f"StringPromptValue 对象: {prompt_value_1}")
print(f"type结果: {type(prompt_value_1)}")
print(f"类名: {prompt_value_1.__class__.__name__}\n")

print(f"ChatPromptValue 对象: {prompt_value_2}")
print(f"type结果: {type(prompt_value_2)}")
print(f"类名: {prompt_value_2.__class__.__name__}\n")

# ===================== 2. 第二种：纯字符串 str =====================
str_prompt = "直接输入的纯文本提示词"
print("===== 2. 纯文本 str 类型 =====")
print(f"内容: {str_prompt}")
print(f"type结果: {type(str_prompt)}\n")

# ===================== 3. 第三种：消息序列 Sequence[MessageLikeRepresentation] 列表 =====================
message_list = [
    ("system", "你是贴心助手"),
    ("human", "今天吃什么")
]
print("===== 3. 消息列表 Sequence(list) 类型 =====")
print(f"内容: {message_list}")
print(f"外层type: {type(message_list)}")
print(f"列表内单个元素类型: {type(message_list[0])}")