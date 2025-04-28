# xp_system.py

class XPSystem:
    def __init__(self):
        self.xp = 0

    def add_xp(self, xp):
        self.xp += xp

    def get_xp(self):
        return self.xp

    def reset_xp(self):
        self.xp = 0
