# daily_task.py

import random
from datetime import date

class DailyTaskManager:
    def __init__(self):
        self.daily_tasks = [
            "Bugün en az 10 dakika meditasyon yap.",
            "En az 15 dakika dışarıda vakit geçir.",
            "Bugün yeni bir şey öğren ve kaydet.",
            "Bir arkadaşına ya da ailene minnettar olduğunu söyle.",
            "Gün içinde en az 2 litre su iç.",
            "Hiçbir dijital cihaz kullanmadan 30 dakika geçir.",
            "Bugün seni mutlu eden 3 şeyi yaz.",
            "Yeni bir egzersiz dene.",
            "Küçük bir iyilik yap ve not al.",
            "Kendi gelişimini öven bir günlük yaz."
        ]
        self.last_shown_date = None
        self.current_task = None

    def get_daily_task(self):
        today = date.today()
        if self.last_shown_date != today:
            self.current_task = random.choice(self.daily_tasks)
            self.last_shown_date = today
        return self.current_task
