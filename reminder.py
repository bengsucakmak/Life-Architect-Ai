# reminder.py

import threading
import time
import random

class Reminder:
    def __init__(self, tasks):
        self.tasks = tasks
        self.running = False

    def start(self, interval_minutes=60):
        self.running = True
        thread = threading.Thread(target=self._remind, args=(interval_minutes,))
        thread.daemon = True
        thread.start()

    def _remind(self, interval_minutes):
        while self.running:
            time.sleep(interval_minutes * 60)
            task = random.choice(self.tasks)
            print("\n🔔 HATIRLATICI: Unutma, bu görevi tamamladın mı?")
            print(f"👉 Görev: {task}\n")

    def stop(self):
        self.running = False
