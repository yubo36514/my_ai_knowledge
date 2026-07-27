from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from pydantic import BaseModel, Field
# 假设你的类叫 InMemoryChatMessageHistory
class InMemoryChatMessageHistory:
    def __init__(self):
        self.messages = []

    class Config:
        arbitrary_types_allowed = True

    # messages: list[BaseMessage] = Field(default_factory=list)

    async def aget_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)

# ========== 1. 实例化对象 ==========
chat_history = InMemoryChatMessageHistory()

# ========== 2. 往列表添加不同类型消息 ==========
# 系统提示词
chat_history.add_message(SystemMessage(content="你是一名Python代码讲解专家"))
# 用户提问
chat_history.add_message(HumanMessage(content="解释dict.get()方法"))
# AI回答
chat_history.add_message(AIMessage(content="dict.get(key, 默认值)，键不存在返回默认值，不抛异常"))

# ========== 3. 两种方式查看列表内容 ==========
## 方式1：直接访问实例属性（最简单，同步）
msg_list = chat_history.messages
print("===== 直接打印消息列表对象 =====")
print(msg_list)

# ## 方式2：调用异步方法 aget_messages()（规范写法，需要await）
# import asyncio
# async def show_msg():
#     msgs = await chat_history.aget_messages()
#     print("\n===== 异步获取的消息列表 =====")
#     print(msgs)
#
# asyncio.run(show_msg())
#
# # ========== 4. 遍历逐条取出内容（最实用） ==========
# print("\n===== 逐条遍历提取角色+文本 =====")
# for msg in chat_history.messages:
#     # msg.type 代表消息类型：system / human / ai
#     # msg.content 代表对话文本内容
#     print(f"【{msg.type}】：{msg.content}")