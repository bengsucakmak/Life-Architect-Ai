# mood_tracking.py

from transformers import pipeline

class MoodTracking:
    def __init__(self):
        # transformers'ın sentiment-analysis pipeline'ı
        self.analyzer = pipeline("sentiment-analysis")

    def track_mood(self, mood_text: str) -> None:
        """
        Kullanıcının ruh halini otomatik analiz eder
        ve uygun öneriyi ekrana basar.
        """
        result = self.analyzer(mood_text)[0]
        label = result["label"]  # POSITIVE veya NEGATIVE
        suggestions = {
            "POSITIVE": "Harika bir ruh halindesin! Yaratıcılığı artıracak görevler öneriyorum.",
            "NEGATIVE": "Biraz rahatlaman iyi olabilir. Rahatlatıcı aktiviteler ekledim."
        }
        suggestion = suggestions.get(label, "Bu ruh haline uygun görevler öneriyorum!")
        print(f"\n🎯 Ruh Halin Analizi: {suggestion}")
