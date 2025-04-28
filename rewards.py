# rewards.py

class RewardsSystem:
    def __init__(self):
        self.rewards = {
            "100": "Bronz Madalya 🥉",
            "500": "Gümüş Madalya 🥈",
            "1000": "Altın Madalya 🥇",
            "5000": "Platin Madalya 🏆",
        }

    def check_rewards(self, xp):
        reward = None
        for xp_threshold, reward_name in sorted(self.rewards.items(), reverse=True):
            if xp >= int(xp_threshold):
                reward = reward_name
                break
        return reward
