import openai
import os


class chat_api:

    def __init__(self, questions: str, max_word: int, temp: float):

        self.question = questions
        self.max_word = max_word
        self.temp = temp

    def ask_question(self):

        openai.api_key = os.getenv('OPENAI_API_KEY')

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.question,
            temperature=self.temp,
            max_tokens=self.max_word,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response
