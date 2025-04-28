# chat_mode.py

from ai_client import AIClient

class ChatMode:
    def __init__(self):
        self.ai = AIClient()

    def chat(self, user_input: str) -> str:
        """
        Kullanıcının girdiği metni LLM'e yollar, dönen cevabı alır.
        """
        return self.ai.chat(user_input, temperature=0.7, max_tokens=150)
