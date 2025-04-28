# pomodoro.py

import time

class Pomodoro:
    def __init__(self, task_name, work_duration=25, break_duration=5):
        self.task_name = task_name
        self.work_duration = work_duration
        self.break_duration = break_duration

    def start_timer(self):
        print(f"\n⏰ {self.task_name} için çalışma süresi başladı!")
        time.sleep(self.work_duration * 60)  # Çalışma süresi
        print(f"🔔 {self.task_name} tamamlandı. Şimdi bir ara ver!")
        time.sleep(self.break_duration * 60)  # Ara süresi
        print("🔁 Ara tamamlandı! Yeni bir döngüye başlamak için hazır ol.")
