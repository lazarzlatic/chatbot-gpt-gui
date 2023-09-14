import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choice[0].text
        return response
