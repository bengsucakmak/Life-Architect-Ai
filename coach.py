# coach.py

from ai_client import AIClient

class Coach:
    def __init__(self):
        self.ai = AIClient()

    def give_development_suggestion(self, user_history: list[str]) -> None:
        """
        Son görev geçmişini alarak LLM'den kişiye özel
        motive edici bir gelişim önerisi ister.
        """
        # Geçmişin son 5 girdisini alıp prompt'u oluşturuyoruz
        history_snippet = "\n".join(user_history[-5:])
        prompt = (
            f"Kullanıcının önceki görev geçmişi:\n{history_snippet}\n\n"
            "Bu kullanıcı için kısa ve motive edici bir gelişim önerisi "
            "cümlesi yaz."
        )
        suggestion = self.ai.chat(prompt, temperature=0.8, max_tokens=60)
        print(f"\n📝 Gelişim Önerisi: {suggestion}")
