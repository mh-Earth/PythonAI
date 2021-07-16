import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pickle
from colorama import Fore
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[2].id)

newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)

'''
This is for AI to speak
'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''
This fuction is use for storge data for AI to do match more corrently
'''
def storeQuery(word):
    e = open('data.pkl','rb')
    datalist = pickle.load(e)
    if word not in datalist:
        datalist.append(word)
    e.close()
    f = open('data.pkl','wb')
    pickle.dump(datalist,f)
    f.close()
    # print(datalist)

'''
This fuction is to load data for AI
'''
def loadCommonWord():
    e = open('data.pkl','rb')
    datalist = pickle.load(e)
    e.close()
    return datalist


'''
This function is use to make pickel file use it on setup or reset the ai data
'''
def makePickle():
    with open ('data.pkl', 'wb') as e:
        pickle.dump([''],e)
        e.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

'''
This function is use to load all avaleable file paths
'''
def loadFilePaths():
    f = open("filePaths.pkl","rb")
    paths  = pickle.load(f)
    f.close()
    # this will return a dictonary  
    return paths

'''
It takes microphone input from the user and returns string output
'''
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.LIGHTGREEN_EX + "Listening..." + Fore.RESET)
        # speak('listening now')
        r.energy_threshold = 700
        r.dynamic_energy_threshold = 1.5
        r.operation_timeout = 5
        r.phrase_threshold = .7
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f'You said:{str(query).lower()}')
        # speak(query)
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        # speak("Say that again please...")  
        return "m"
    return query


checkList = ["javis","hello","are you listening"]
ramWarning = True
