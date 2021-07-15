import time
import psutil
# from main import speak
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

WarningNow = True
WarningNum = 0

def ramWarnings():
    time.sleep(1)
    global WarningNum ,WarningNow
    if WarningNow:
        if round(psutil.virtual_memory()[2]) > 90:
            speak('Sir you ram is in high use')
            WarningNum+=1

            if WarningNum > 3:
                speak(f'This is {WarningNum}th warning')
    
    elif round(psutil.virtual_memory()[2]) < 55:
        WarningNum = 0
        WarningNow = True

if __name__ == "__main__":
    pass

