# ai_client.py  

import os
from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL_NAME

class AIClient:
    def __init__(self):
        # Ortam değişkeni olarak ayarla, OpenAI() bunları otomatik kullanacak
        os.environ["OPENAI_API_KEY"] = API_KEY
        os.environ["OPENAI_API_BASE"] = BASE_URL

        # Parametresiz init — SDK, env değişkenlerinden okur
        self.client = OpenAI()
        self.model = MODEL_NAME

    def chat(self, prompt: str, **kwargs) -> str:
        """
        Tek bir kullanıcı mesajı alır, LLM'e gönderir ve yanıtını döner.
        kwargs: temperature, max_tokens, vs. gibi parametreleri alabilir.
        """
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return resp.choices[0].message.content
