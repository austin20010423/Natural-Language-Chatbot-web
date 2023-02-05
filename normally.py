import gpt


class chat_normally:

    def __init__(self, ask, ans_num, diversity):
        self.ask = ask
        self.ans_num = ans_num
        self.diversity = diversity

    def talk(self):

        ans = gpt.chat_api(self.ask, self.ans_num, self.diversity)
        return ans.ask_question()['choices'][0]['text']

    def save(self):

        previous = self.talk()
        return previous
