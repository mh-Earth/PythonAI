import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import sys,time
import pywhatkit as kit
import pyautogui
import threading
import psutil
import pickle
from ramWarnings import ramWarnings
from colorama import Fore
from wordMacth import find_most_common_match
import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[2].id)

newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def loadCommonWord():
    e = open('data.pkl','rb')
    datalist = pickle.load(e)
    e.close()
    return datalist



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

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.LIGHTGREEN_EX + "Listening..." + Fore.RESET)
        # speak('listening now')
        r.energy_threshold = 400
        r.pause_threshold = 1.5 
        r.operation_timeout = 5
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
def main():
    global ramWarning
    sayError = True
    while True:
        if ramWarning:
            ramWarnings()
        query = takeCommand().lower()
        if 'search' in query:
            query = query[7:]
            kit.search(query)
            print(query)

        elif query == "m":
            pass
        
        elif query in checkList:
            speak('yes sir')
            storeQuery(str(query))

        elif 'info' in query:
            try:
                query = query[5:]
                info = kit.info(query,return_value=True)
                speak(f'accoding to wikipidia {info}')
                print(query)
            except Exception as e:
                speak("There is an error to searching wikipidia")
                speak("And the error says")
                speak(e)
        elif query == 'reset data':
            makePickle()

        elif query.startswith('open localhost'):
            a = len('open localhost')
            print(a)
            if len(query) == a: 
                speak('which port sir')
                portNum = takeCommand().lower()
                webbrowser.open_new_tab(f'http://localhost:{portNum}')
                storeQuery(str(query))

            else:
                portNum = query[a:]
                webbrowser.open_new_tab(f'http://localhost:{portNum}')
                storeQuery(str(query))

        elif query == "open task manager":
            os.startfile('C:\\Windows\\System32\\Taskmgr.exe')
            speak("opening task manager")

        elif query == "open control panel":
            os.startfile('C:\\Users\\User\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk')
            storeQuery(str(query))

        elif query == "open firefox":
            os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            storeQuery(str(query))
        
        elif query == "open vs code":
            os.startfile('C:\\Program Files\\Microsoft VS Code\\Code.exe')
            storeQuery(str(query))
        
        elif query == "open powershell":
            os.startfile('C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe')
            storeQuery(str(query))
        
        elif query == "open camera":
            os.startfile('C:\\Users\\User\\Desktop\\Camera.lnk')
            storeQuery(str(query))

        elif query == "open bandicam":
            os.startfile('C:\\Program Files\\Bandicam\\bdcam.exe')
            storeQuery(str(query))
        
        elif query.endswith('.com') or query.endswith('dotkom'):
            if query.endswith("dotkom"):
                query = query[:-7]
                query = query + ".com"
            query = query[5:]
            
            try:
                requests.post(f'https://www.{query}')
                webbrowser.open_new_tab(f"www.{query}")
                storeQuery(f"open {str(query)}")

            except Exception as e:
                print(f'https://www.{query} not found sir')
                speak(f'www.{query} not found sir')
                break
            speak("opening" + query)
            # webbrowser.open_new
            # kit.search(query)
            print(query)

        
        elif query == "exit" or query == 'shutdown':
            speak("Exiting sir")
            storeQuery(str(query))
            sys.exit()
                    
        elif query.startswith('close'):
            query = query[5:]
            if query == 'vs code':
                speak(f'closeing {query}')
                os.system("TASKKILL /F /IM code.exe") 

            else:
                speak(f'closeing {query}')
                os.system(f"TASKKILL /F /IM {(query).lower()}.exe") 

        elif query.startswith('start'):
            storeQuery(str(query))
            query = query[5:]
            os.system(query)


        elif query.startswith('run'):
            storeQuery(str(query))
            query = query[3:].lower()
            os.system(query)
        
        elif query.startswith('reload'):
            storeQuery(str(query))
            speak('reloading current page')
            pyautogui.press('f5')
        
        elif query == 'ram status' or query ==  'memory status':
            ramstatus = round(psutil.virtual_memory()[2])
            speak(f'Ram is on {ramstatus}% use' )
            storeQuery(str(query))

        
        elif query ==  'stop ram warning' or query == 'stop memory warning':
            ramWarning = False
            speak('stoping ram warnings')
            storeQuery(str(query))
        
        elif query == "mute":
            pass

        else:
            mWords = loadCommonWord()
            # print(mWords)
            mostMatchingWord = find_most_common_match(query,mWords)
            # print(mostMatchingWord)
            try:
                speak(f'Most matching quary found {mostMatchingWord[0][0]} and {mostMatchingWord[1][0]}')
                # sayError = False
            except Exception as indexError:
                try:
                    speak(f'Most matching quary found {mostMatchingWord[0][0]}')
                except Exception as e:
                    if sayError:
                        speak(f"No matching quary found -> {query}")
            main()       
            
        
                    


        
if __name__ == "__main__":
    # wishMe()
    main()
    # storeQuery('meherab')