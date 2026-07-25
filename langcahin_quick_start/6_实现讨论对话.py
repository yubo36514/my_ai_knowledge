from langchain_community.chat_models import ChatTongyi

class MutiTurnChat():
    def __init__(self, model, system_prompt,streaming=True):
        self.llm=ChatTongyi(model=model, streaming=streaming)
        self.chat_history=[]
        if system_prompt:
            self.chat_history.append(('system',system_prompt))

    def add_user_message(self, content):
        self.chat_history.append(('user',content))

    def add_ai_message(self, content):
        self.chat_history.append(('ai',content))

    def send(self):

        full_reply = ""
        result=self.llm.stream(input=self.chat_history)
        for chunk in result:
            print(chunk.content,end='', flush=True)
            full_reply += chunk.content
        print()

        self.add_ai_message(full_reply)





if __name__ == '__main__':
    model='qwen3-max'
    system_prompt='你是一个非常出色的ai老师'
    chat=MutiTurnChat(model,system_prompt)
    while True:
        user_input=input('用户：')
        if user_input.strip() in ['exit', 'quit']:
            print('对话结束')
            break
        if not user_input.strip():
            print('请勿输入空白内容')
            continue
        chat.add_user_message(user_input)
        chat.send()
