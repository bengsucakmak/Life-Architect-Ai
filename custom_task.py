# custom_task.py

import time

class CustomTask:
    def __init__(self, title, description, difficulty, estimated_time, project_goal):
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.estimated_time = estimated_time
        self.project_goal = project_goal
        self.is_completed = False

    def complete_task(self):
        self.is_completed = True
        print(f"✅ {self.title} görevi tamamlandı!")
        return self.is_completed

    def get_task_info(self):
        return {
            "Başlık": self.title,
            "Açıklama": self.description,
            "Zorluk Seviyesi": self.difficulty,
            "Tahmin Edilen Zaman": f"{self.estimated_time} dakika",
            "Proje Hedefi": self.project_goal
        }

    def start_task(self):
        print(f"\n🔧 {self.title} görevi başladı!")
        time.sleep(self.estimated_time * 60)  # Zamanı dakika cinsinden alıp bekletiyor
        print(f"⏱️ {self.title} görevi tamamlandı!")
        self.complete_task()
