# analytics.py

import json
import os
import matplotlib.pyplot as plt

class AnalyticsManager:
    def __init__(self, filename="xp_history.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def save_xp(self, xp_amount):
        history = self.load_xp_history()
        history.append(xp_amount)
        with open(self.filename, 'w') as f:
            json.dump(history, f, indent=4)

    def load_xp_history(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def plot_xp_progress(self):
        xp_history = self.load_xp_history()
        if not xp_history:
            print("📉 Henüz XP geçmişi yok, grafik oluşturulamıyor.")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(xp_history)+1), xp_history, marker='o', linestyle='-', color='purple')
        plt.title('🧪 XP Kazanım Grafiği')
        plt.xlabel('Görev Sayısı')
        plt.ylabel('XP Miktarı')
        plt.grid(True)
        plt.show()
