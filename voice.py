# voice.py

import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)  # Konuşma hızı (default 200)
        self.engine.setProperty('volume', 1)  # Ses seviyesi (0.0 ile 1.0 arası)
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def set_voice(self, gender="female"):
        voices = self.engine.getProperty('voices')
        if gender == "female":
            self.engine.setProperty('voice', voices[1].id)  # Kadın sesi
        else:
            self.engine.setProperty('voice', voices[0].id)  # Erkek sesi
