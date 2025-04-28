# goal_setting.py

class GoalSetting:
    def __init__(self, user_level):
        self.user_level = user_level

    def suggest_goals(self):
        if self.user_level == "beginner":
            return "Başlangıç seviyesi hedefi: 5 kolay görev tamamla."
        elif self.user_level == "intermediate":
            return "Orta seviyede hedef: 10 orta seviye görev tamamla."
        elif self.user_level == "advanced":
            return "İleri seviyede hedef: 15 zor görev tamamla."
        else:
            return "Hedef belirleme başarılı bir yolculuğun başlangıcıdır!"
