from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# --------------------------
# 一、狭义老式LLM 对应规则
# --------------------------
print("===== 1. 狭义LLM（文本补全模型）规则 =====")
# 1. 直接invoke调用：规定传入 str 字符串
direct_input_llm = "直接给老式LLM的纯文本提示词"
print(f"老式LLM直接调用合法入参类型：{type(direct_input_llm)}")

# 2. LCEL链路：模板渲染产出 StringPromptValue（属于PromptValue）
llm_template = PromptTemplate.from_template("请回答：{query}")
llm_prompt_value = llm_template.invoke({"query": "测试问题"})
llm=Tongyi(model="qwen-max")
chain=llm_template | llm
print(f"LCEL链式传递对象类型：{type(llm_prompt_value)}")
print(f"类名称：{llm_prompt_value.__class__.__name__}\n")

# --------------------------
# 二、Chat对话模型 对应规则
# --------------------------
print("===== 2. Chat聊天对话模型规则 =====")
# 1. 直接invoke调用：规定传入 消息列表list
direct_input_chat = [
    ("system", "你是专业助手"),
    ("human", "今天天气怎么样")
]
print(f"Chat模型直接调用合法入参外层类型：{type(direct_input_chat)}")

# 2. LCEL链路：模板渲染产出 ChatPromptValue（属于PromptValue）
chat_template = ChatPromptTemplate.from_messages([
    ("system", "你擅长{skill}"),
    ("human", "帮我解答问题")
])
chat_prompt_value = chat_template.invoke({"skill": "Python编程"})
print(f"LCEL链式传递对象类型：{type(chat_prompt_value)}")
print(f"类名称：{chat_prompt_value.__class__.__name__}")