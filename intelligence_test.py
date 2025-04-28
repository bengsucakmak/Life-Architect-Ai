# intelligence_test.py

import random

class IntelligenceTest:
    def __init__(self):
        self.questions = [
            {"question": "Bir tren, 60 km/s hızla 120 km yol alacaksa, kaç saat sonra varır?", "answer": 2},
            {"question": "5, 10, 15, 20, ?, 30, 35. Soru işaretinin yerine hangi sayı gelir?", "answer": 25},
            {"question": "Bir çiftlikte 4 tavuk ve 6 inek var. Toplamda kaç bacak var?", "answer": 28},
            {"question": "Bir otobüs 8 saat sonra 240 km yol alırsa, saatte kaç km yol alır?", "answer": 30},
            {"question": "Bir sayının 3 katı, 15'in 2 katından 5 fazla ise, bu sayı nedir?", "answer": 10},
        ]

    def start_test(self):
        score = 0
        print("💡 Zeka Testine Hoş Geldiniz! 💡\n")
        random.shuffle(self.questions)

        for q in self.questions:
            print(f"Soru: {q['question']}")
            try:
                user_answer = int(input("Cevabınız: "))
            except ValueError:
                user_answer = None

            if user_answer == q['answer']:
                print("✅ Doğru!")
                score += 1
            else:
                print(f"❌ Yanlış. Doğru cevap: {q['answer']}")

        print(f"\n🎯 Test Sonucu: {score}/{len(self.questions)} doğru cevap!")
        return score
