# history.py

import json
import os

class HistoryManager:
    def __init__(self, filename="history.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def save_task(self, task_text):
        history = self.load_history()
        history.append({"task": task_text})
        with open(self.filename, 'w') as f:
            json.dump(history, f, indent=4)

    def load_history(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def show_history(self):
        history = self.load_history()
        if not history:
            print("📂 Henüz kayıtlı görev yok.")
        else:
            print("\n📜 Geçmiş Görevlerin:")
            for idx, entry in enumerate(history, 1):
                print(f"{idx}. {entry['task']}")
