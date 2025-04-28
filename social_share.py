# social_share.py

class SocialShare:
    def __init__(self, task, xp):
        self.task = task
        self.xp = xp

    def share_on_social_media(self):
        print(f"\n🎉 {self.task} görevi tamamlandı!")
        print(f"XP Kazanıldı: {self.xp}")
        print("📝 Sosyal medyada paylaşmak için bağlantı oluşturuluyor...")
        # Sosyal medya paylaşım bağlantısı oluştur
        # Bu kısmı örnek olarak bırakıyoruz; gerçek API entegrasyonu burada yapılabilir
        print(f"🔗 Paylaşılabilir bağlantı: www.socialshare.com/share/{self.task}")
