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
    print(macthingWords)
    return macthingWords


def find_most_common_match(word,allWordList=list):
    mostCommonmatchList = filterMatch(word,allWordList)



    
    matchRatio = []
    for commonWords in mostCommonmatchList:
        llLIist = []

        matchingRatio = difflib.SequenceMatcher(None, word, commonWords).ratio()

        llLIist.append(commonWords)
        llLIist.append(matchingRatio)
        matchRatio.append(llLIist)
        # matchRatio.append(matchingRatio)

        # matchRatio = matchRatio.sorted()
        # print(matchingRatio)
        matchRatio.sort(reverse=True)
    return matchRatio



if __name__ == "__main__":
    # b = find_most_common_match('meherab google osama',allquarys)
    # print(b)
    pass 