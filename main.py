import webbrowser
import os
import sys
import pywhatkit as kit
import pyautogui
import psutil
from ramWarnings import ramWarnings
from colorama import Fore
from wordMacth import find_most_common_match
import requests
from AIFucntions import *
from FindAllPaths import storePaths_Stealth

'''
This is the main fucntion or the core of AI
'''

def main():
    global ramWarning
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
        
        
        elif query.startswith("find"):
            fileDirName = query[5:]
            findingPath = findFile(fileDirName)
            if findingPath != None:
                print(f'sir File name {fileDirName} found in {findingPath}')
                speak(f'sir File name {fileDirName} found in {findingPath}')


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
            appName = query[5:]
            if appName == 'vs code':
                speak(f'closeing {query}')
                os.system("TASKKILL /F /IM code.exe") 

            else:
                try:
                    # appName = query[5:].replace("dot",".")
                    appName = query[6:]
                    if " dot " in appName:
                        appName = appName.replace(" dot ",".")
                    appName = appName.replace(" ","")

                    print(appName)
                    allFilePaths = loadFilePaths()
                    listTomatchWord = list(allFilePaths.keys())
                    
                    # print(listTomatchWord)
                    matchratio = find_most_common_match(appName,listTomatchWord,findCommonWord=False)
                    try:
                        print(f"Most matching word found {matchratio[0][1]} {matchratio[0][0]}  and {matchratio[1][1]} {matchratio[1][0]}%")
                        # speak(f"Most matching word found {matchratio[0][1]}  and {matchratio[1][1]} ")


                        os.close(allFilePaths[str(matchratio[0][1])])
                    except Exception as e:
                        
                        try:
                            print(f"Most matching word found {matchratio[0][0]} {matchratio[0][1]}%")
                            # speak(f"Most matching word found {matchratio[0][0]}")
                            os.close(allFilePaths[matchratio[0][1]])
                        except Exception as e:
                            # print(matchratio)
                            print(e)
                            print("No matching quary found")
                            speak("No matching quary found")

                        # speak("")
                    # os.startfile(quaryPath)

                except Exception as e:
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

        elif query.startswith('open'):
            # appName = query[5:].replace("dot",".")
            appName = query[5:]
            if " dot " in appName:
                appName = appName.replace(" dot ",".")
            appName = appName.replace(" ","")

            print(appName)
            allFilePaths = loadFilePaths()
            listTomatchWord = list(allFilePaths.keys())
            
            # print(listTomatchWord)
            matchratio = find_most_common_match(appName,listTomatchWord,findCommonWord=False)
            # print(matchratio)
            print(matchratio)
            try:
                if matchratio[0][0] > .60:
                    print(f"Most matching word found {matchratio[0][1]} {matchratio[0][0]}  and {matchratio[1][1]} {matchratio[1][0]}%")
                    # speak(f"Most matching word found {matchratio[0][1]}  and {matchratio[1][1]} ")
                    os.startfile(allFilePaths[str(matchratio[0][1])])
                else:
                    raise indexError

            except Exception as e:
                
                try:
                    if matchratio[0][0] > .40:
                        print(f"Most matching word found {matchratio[0][0]} {matchratio[0][1]}%")
                        # speak(f"Most matching word found {matchratio[0][0]}")
                        os.startfile(allFilePaths[matchratio[0][1]])
                    else:
                        raise indexError
                except Exception as e:
                    # print(matchratio)
                    print(e)
                    print("No matching quary found")
                    speak("No matching quary found")

                # speak("")
            # os.startfile(quaryPath)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        else:
            mWords = loadCommonWord()
            # print(mWords)
            mostMatchingWord = find_most_common_match(query,mWords,findCommonWord=False)
            # print(mostMatchingWord)
            try:
                if mostMatchingWord[0][0] > .50:
                    print(f'Most matching quary found {mostMatchingWord[0][1]} and {mostMatchingWord[1][1]}')
                    print(f'Most matching quary found {mostMatchingWord[0][0]} and {mostMatchingWord[1][0]}')
                    speak(f'Most matching quary found {mostMatchingWord[0][1]} and {mostMatchingWord[1][1]}')
                else:
                    raise indexError
            except Exception as indexError:
                try:
                    if mostMatchingWord[0][0] > .40:

                        print(f'Most matching quary found {mostMatchingWord[0][1]}')
                        print(f'Most matching quary found {mostMatchingWord[0][0]}')
                        speak(f'Most matching quary found {mostMatchingWord[0][1]}')
                    else:
                        raise IndexError
                except Exception as e:
                    speak(f"No matching quary found -> {query}")
            main()       
            
        
                    


        
if __name__ == "__main__":
    print(Fore.GREEN + "Starting up......." + Fore.RESET)
    # wishMe()
    # speak('Listening Now')
    storePaths_Stealth()
    try:
        main()
    except Exception as e:
        print(e)
        main()