# modes.py

class ModeManager:
    def __init__(self):
        self.modes = {
            "Sakin Mod": {"task_multiplier": 1},
            "Hızlı İlerleme Modu": {"task_multiplier": 2},
            "Yoğun Rehberlik Modu": {"task_multiplier": 3}
        }
        self.current_mode = "Sakin Mod"

    def select_mode(self):
        print("\n🚀 Mevcut Modlar:")
        for mode in self.modes:
            print(f"- {mode}")
        selected = input("\nHangi modu seçmek istersin? : ")

        if selected in self.modes:
            self.current_mode = selected
            print(f"\n✅ {selected} aktif edildi!\n")
        else:
            print("\n⚠️ Geçersiz seçim. Sakin Mod aktif edildi.\n")
            self.current_mode = "Sakin Mod"

    def get_multiplier(self):
        return self.modes[self.current_mode]["task_multiplier"]
