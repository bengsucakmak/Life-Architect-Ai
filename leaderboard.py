# leaderboard.py

class Leaderboard:
    def __init__(self):
        self.scores = {}

    def add_score(self, username, score):
        self.scores[username] = score
        self.display_leaderboard()

    def display_leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print("\n🏆 Liderlik Tablosu: ")
        for rank, (username, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {username}: {score} XP")
