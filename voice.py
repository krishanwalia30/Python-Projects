import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(tex):
     tts = gTTS(text=tex, lang="en")
     filename = "voice.mp3"
     tts.save(filename)
     playsound.playsound(filename)
     os.remove(filename)
def get_audio():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          audio = r.listen(source,phrase_time_limit=3)
          said = ''
          try:
               said = r.recognize_google(audio)
               return said
          except Exception as e:
               print("EXCEPTION:",str(e))



