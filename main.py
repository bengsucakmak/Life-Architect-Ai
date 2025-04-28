from tasks import generate_tasks
from xp_system import XPSystem
from modes import ModeManager
from history import HistoryManager
from voice import VoiceAssistant
from analytics import AnalyticsManager
from coach import Coach
from daily_task import DailyTaskManager
from reminder import Reminder
from chat_mode import ChatMode
from rewards import RewardsSystem
from intelligence_test import IntelligenceTest
from custom_task import CustomTask


def detect_difficulty(task_text: str) -> str:
    txt = task_text.lower()
    if "kolay" in txt:
        return "kolay"
    elif "orta" in txt:
        return "orta"
    elif "zor" in txt:
        return "zor"
    else:
        return "diğer"


def main():
    print("✨ Evrensel Rehber AI'ye hoş geldin! ✨\n")

    # Bugünün özel görevi
    daily_task_manager = DailyTaskManager()
    daily = daily_task_manager.get_daily_task()
    print(f"🎯 Bugünün Özel Görevi: {daily}\n")

    # Mod seçimi
    mode_manager = ModeManager()
    mode_manager.select_mode()

    # Kullanıcı hedefi ve ruh hali
    user_goal = input("Hayattaki şu anki hedefin nedir?: ")
    user_mood = input("Bugün ruh halin nasıl? (mutlu, üzgün, stresli, motive, vs.): ")
    print("\n📚 Kişisel rehberin hazırlanıyor...\n")

    multiplier = mode_manager.get_multiplier()
    results = generate_tasks(user_goal, user_mood, multiplier)

    xp_system = XPSystem()
    history_manager = HistoryManager()
    voice_assistant = VoiceAssistant()
    analytics_manager = AnalyticsManager()
    coach = Coach()
    reminder = Reminder(results)
    chat_mode = ChatMode()
    rewards_system = RewardsSystem()
    intelligence_test = IntelligenceTest()

    # Özellik tercihleri
    use_voice = input("Görevlerin sesli okunmasını ister misin? (evet/hayır): ").lower()
    use_coach = input("Kişisel koç desteğini açmak ister misin? (evet/hayır): ").lower()
    use_reminder = input("Görev Hatırlatıcıyı açmak ister misin? (evet/hayır): ").lower()
    use_chat_mode = input("Sohbet modunu açmak ister misin? (evet/hayır): ").lower()
    use_int_test = input("Zeka testini başlatmak ister misin? (evet/hayır): ").lower()

    # Yeni özel görev oluşturma
    if input("Özel görev oluşturmak ister misin? (evet/hayır): ").lower() == "evet":
        title = input("Görev Başlığı: ")
        desc = input("Görev Açıklaması: ")
        diff = input("Görev Zorluk Seviyesi (kolay/orta/zor): ").lower()
        est = int(input("Tahmin Edilen Süre (dakika): "))
        goal = input("Bu görevin proje/hedef amacı nedir?: ")

        custom = CustomTask(title, desc, diff, est, goal)
        info = custom.get_task_info()
        print("\n📋 Özel Görev Bilgileri:")
        for k, v in info.items():
            print(f"- {k}: {v}")

        if input("Görevi şimdi başlatmak ister misin? (evet/hayır): ").lower() == "evet":
            custom.start_task()
            xp_gain = 20 if diff == "kolay" else 50 if diff == "orta" else 100
            xp_system.add_xp(xp_gain)
            analytics_manager.save_xp(xp_gain)
            history_manager.save_task(title)
            print(f"🎉 Özel görev tamamlandı, kazandığın XP: {xp_gain}")

    # Sesli asistan ayarı
    if use_voice == "evet":
        gender = input("Ses türü seç (female/male): ").lower()
        voice_assistant.set_voice(gender)

    # Hatırlatıcı başlat
    if use_reminder == "evet":
        try:
            interval = int(input("Kaç dakikada bir hatırlatma yapmak istersin?: "))
        except ValueError:
            interval = 60
        reminder.start(interval_minutes=interval)

    print("\n🧭 Evrensel Rehber Planın Hazır!\n")

    # Görevlerin yerine getirilmesi
    for task in results:
        print(f"\nGörev: {task}\n")

        if use_voice == "evet":
            voice_assistant.speak(task)

        comp = input("✅ Bu görevi tamamladın mı? (evet/hayır): ").lower()
        while comp not in ["evet", "hayır"]:
            comp = input("Lütfen sadece 'evet' veya 'hayır' yaz: ").lower()

        if comp == "evet":
            difficulty = detect_difficulty(task)
            xp_val = 10 * (1 if difficulty == "kolay" else 2 if difficulty == "orta" else 3)
            xp_system.add_xp(xp_val)
            analytics_manager.save_xp(xp_val)
            history_manager.save_task(task)
            print(f"🎉 Tebrikler! Bu görevden {xp_val} XP kazandın. Toplam XP: {xp_system.get_xp()}")
            if use_coach == "evet":
                coach.give_development_suggestion(difficulty)
        else:
            print("⏳ Tamamlamadığın görevleri daha sonra tekrar yapabilirsin.")

    # Zeka testi
    if use_int_test == "evet":
        score = intelligence_test.start_test()
        print(f"🎯 Test Sonucu: {score}/{len(intelligence_test.questions)} doğru cevap!")
        xp_system.add_xp(score * 10)
        analytics_manager.save_xp(score * 10)

    # Ödül kazanma
    reward = rewards_system.check_rewards(xp_system.get_xp())
    if reward:
        print(f"\n🎁 Yeni Ödül Kazandın: {reward}")

    print(f"\n🏆 Toplam XP Puanın: {xp_system.get_xp()}")
    print(f"🔮 Seviye: {xp_system.level() if hasattr(xp_system, 'level') else '1'}")

    # Geçmiş görevleri göster
    if input("\n📖 Geçmiş görevleri görmek ister misin? (evet/hayır): ").lower() == "evet":
        history_manager.show_history()

    # XP grafiği göster
    if input("\n📊 XP ilerleme grafiğini görmek ister misin? (evet/hayır): ").lower() == "evet":
        analytics_manager.plot_xp_progress()

    reminder.stop()


if __name__ == "__main__":
    main()
