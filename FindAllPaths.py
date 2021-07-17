'''
This is the files for finding all the paths in a desvice to open by the AI
Some file paths will not be store like .git , .pyc , __init__ 
'''

import os
import pickle
from colorama import Fore

userName = 'User' #replace This with your user name

pucList = ["!","@","#","$","%","^","&","|","*","(",")","-","+","_","=","[","{","]","}",";",":","'",'"',"\\","<",",",">","/","?"," "]
pathDict = {}
def removePuc(word=str):
    # for puc in pucList:
    for i in range(len(pucList)):
        word = word.replace(pucList[i],"")
        # print(pucList[i] ,word)
    return word

def find(path,debug=False): 
    # print(f"searching path {path}\n\n")
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if ".git" not in os.path.join(root, name):
                if "__pycache__" not in os.path.join(root, name):
                    if "migrations" not in os.path.join(root, name):
                        if "\My" not in os.path.join(root, name):
                            name = removePuc(name)
                            pathDict.update({str(name).lower():os.path.join(root, name)})
                            if debug:
                                print(name , os.path.join(root, name))
                                # print({name:os.path.join(root, name)})

        for name in files:
            if ".git" not in os.path.join(root, name):
                if ".pyc" not in os.path.join(root, name):
                    if "__init__" not in os.path.join(root, name):
                        if "migrations" not in os.path.join(root, name):
                            if "\My" not in os.path.join(root, name):
                                name = removePuc(name)
                                pathDict.update({str(name).lower():os.path.join(root, name)})
                                if debug:
                                    print(name ,os.path.join(root, name))

        # print(files)
        # if name in files:
        # elif name in dirs:
        #     return os.path.join(root, name)



    

def stroePaths():
    
    pathJoinList = ['Desktop', 'Documents', 'Downloads', 'Favorites', 'Music','Pictures','Templates', 'Videos']
    print(Fore.LIGHTRED_EX + "Finding all Paths" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "")

    f = open('filePaths.pkl','wb')
    # f = open('filePaths.txt','w')

    for item in pathJoinList:
        find(f"c:\\Users\\{userName}\\{item}",debug=True)
        pathDict.update({item:f"c:\\Users\\{userName}\\{item}"})
        # print(item)

    # f.write(str(pathDict))
    pickle.dump(pathDict,f)

    f.close()    

    print( 'Done.........' + Fore.RESET)

def storePaths_Stealth():
    
    pathJoinList = ['Desktop', 'Documents', 'Downloads', 'Favorites', 'Music','Pictures','Templates', 'Videos']

    f = open('filePaths.pkl','wb')
    # f = open('filePaths.txt','w')

    for item in pathJoinList:
        find(f"c:\\Users\\{userName}\\{item}")
        pathDict.update({item:f"c:\\Users\\{userName}\\{item}"})
        # print(item)

    # f.write(str(pathDict))
    pickle.dump(pathDict,f)

    f.close()    

if __name__ == "__main__":
    
    stroePaths()