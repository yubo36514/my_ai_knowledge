from openai import OpenAI


client=OpenAI(
    base_url="https://ws-xnlgatus0aaqvdlt.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

completion=client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[
        {
            'role':'system',
            'content':'你是一个助手'
        },
        {
            'role':'user',
            'content':'今天天气如何'
        }
    ]
)
print(completion.choices[0].message.content)