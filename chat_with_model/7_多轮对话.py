from openai import OpenAI

class MutiTurnChat:
    def __init__(self, model_name: str, base_url: str, system_prompt: str = None):
        self.model_name = model_name
        self.client=OpenAI(base_url=base_url)
        self.chat_history = []

        if system_prompt:
            self.chat_history.append({'role': 'system', 'content': system_prompt})


    def add_user_message(self, message):
        if message:
            self.chat_history.append({'role': 'user', 'content': message})

    def add_assistant_message(self, message):
        if message:
            self.chat_history.append({'role': 'assistant', 'content' : message})

    def get_response(self):

        self.add_user_message(user_input)

        model_completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.chat_history
        )

        reply = model_completion.choices[0].message.content
        self.add_assistant_message(model_completion)
        return reply

    def get_history(self):
        return self.chat_history


if __name__ == '__main__':
    model_name = "qwen3.7-plus"
    base_url = "https://ws-xnlgatus0aaqvdlt.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
    system_prompt = "你是一个ai助手"

    chat = MutiTurnChat(model_name, base_url, system_prompt)

    while True:
        user_input = input("用户：")
        if user_input == "":
            continue
        if user_input in ("exit", "quit"):
            break

        print("AI：", chat.get_response())

#
#
