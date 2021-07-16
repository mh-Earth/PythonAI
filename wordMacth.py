import re
import difflib



def filterMatch(wordtoSeacrh,wordList):
    macthingWords = []
    wordtoSeacrh = str(wordtoSeacrh).lower()
    try:
        wordtoSeacrh = str(wordtoSeacrh).split(" ")
    except Exception as e:
        wordtoSeacrh = wordtoSeacrh
    
    for splitWords in wordtoSeacrh:
        for index ,word in enumerate(wordList):
            if  re.search(splitWords ,word) != None:
                if wordList[index] not in macthingWords:
                    macthingWords.append(wordList[index])
    # print(macthingWords)
    return macthingWords


def find_most_common_match(word,allWordList=list,findCommonWord=False): 
    '''
    This match function will take a word and a word list and return a list of list when the
    first item will be the matching ratio and 2nd item will be the most matching word and so on
    '''
    if findCommonWord:
        mostCommonmatchList = filterMatch(word,allWordList)
    else:
        mostCommonmatchList = allWordList



    
    matchRatio = []
    for commonWords in mostCommonmatchList:
        llLIist = []
        # print(commonWords)
        matchingRatio = difflib.SequenceMatcher(None, word, commonWords).ratio() #!importein
        # print(matchingRatio)
        llLIist.append(matchingRatio)
        llLIist.append(commonWords)
        matchRatio.append(llLIist)
        
        matchRatio.sort(reverse=True)
        # print(matchRatio ,"\n\n")
    return matchRatio



if __name__ == "__main__":
    # b = find_most_common_match('meherab google osama',allquarys)
    # print(b)
    pass 