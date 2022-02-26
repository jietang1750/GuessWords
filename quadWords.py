# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import Levenshtein as lev

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def replaceCharacterInString(strWord,strChar,n):
    tmpWord = ''
    if n <= len(strWord) and len(strChar) == 1:
        for i in range(0,len(strWord)):
            if i != n - 1:
                tmpWord = tmpWord + strWord[i]
            else:
                tmpWord = tmpWord + strChar
    elif len(strChar)  == 1:
        tmpWord =word + strChar
    else:
        tmpWord = word + strChar
    return(tmpWord)

def isWord(word,dictionary):
    if word in dictionary[word[0]]:
        return True
    else:
        return False

def clue(pool,confirmedChars,dictionary):
    word = ''
    wordList = []
    i = 0
    for i0 in range(0, len(pool[0])):
        word0 = pool[0][i0]
        # print("1",i1,word)
        for i1 in range(0, len(pool[1])):
            word1 = word0 + pool[1][i1]
            # print("2", i2, word)
            for i2 in range(0, len(pool[2])):
                word2 = word1 + pool[2][i2]
                # print("3", i3, word)
                for i3 in range(0, len(pool[3])):
                    word3 = word2 + pool[3][i3]
                    # print("4", i4, word)
                    for i4 in range(0, len(pool[4])):
                        word4 = word3 + pool[4][i4]
                        word = word4
                        bConfirm = True
                        for k in range(0, len(confirmedChars)):
                            tmpChar = confirmedChars[k]
                            if (tmpChar not in word) and bConfirm:
                                bConfirm = False
                                # print("no", i1, i2, i3, i4, i5, word)
                                break
                        if bConfirm:
                            bWord = isWord(word, dict)
                            # print("yes", i1, i2, i3, i4, i5, word)
                            # print(wordList,word)
                            if bWord:
                                i += 1
                                wordList.append(word)
    return(wordList)

def list2dict(wordList):
    wordDict = {}
    for word in wordList:
        if word[0] not in wordDict.keys():
            wordDict[word[0]] = []
        wordDict[word[0]].append(word)
    return wordDict

def formPool(whiteChar,yellowChar,greenChar):
    pool=[]
    conChar = ''
    yPool = decompChar(yellowChar)
    gPool = decompChar(greenChar)
    # print ("gPool",gPool)
    # print ("yPool",yPool)
    for k in range (1,6):
        tmpPool1 = whiteChar
        for n in yPool.keys():
            for tmpChar in yPool[n]:
                if tmpChar not in tmpPool1:
                    tmpPool1 = tmpPool1 + tmpChar
                if tmpChar not in conChar:
                    conChar = conChar + tmpChar
        for n in gPool.keys():
            for tmpChar in gPool[n]:
                if tmpChar not in tmpPool1:
                    tmpPool1 = tmpPool1 + tmpChar
                if tmpChar not in conChar:
                    conChar = conChar + tmpChar
        if k in gPool.keys():
            tmpPool1 = gPool[k]
            if tmpPool1 not in conChar:
                conChar = conChar + tmpPool1
        if k in yPool.keys():
            for tmpChar in yPool[k]:
                if tmpChar in tmpPool1:
                    tmpPool2 = tmpPool1.replace(tmpChar,'')
                    tmpPool1 = tmpPool2
        pool.append(tmpPool1)

    return (pool,conChar)

def decompChar(strColChar):
    colChar ={}
    for i in range(1,len(strColChar)+1):
        tmpChar = strColChar[i-1]
        if tmpChar.isnumeric():
            nCol = int(tmpChar)
            #print (nCol)
            if nCol not in colChar.keys():
                colChar[nCol] = ''
            # print("numb", tmpChar)
        else:
            if tmpChar not in colChar[nCol]:
                colChar[nCol] = colChar[nCol] + tmpChar
            # print("alpha", tmpChar)
    return (colChar)

def removeCharFromWChar(wChar,word):
    tmpPool = wChar
    for tmpChar in word:
        if tmpChar in tmpPool:
            tmpPool1 = tmpPool.replace(tmpChar,'')
            tmpPool = tmpPool1
            # print(tmpChar,tmpPool,tmpPool1)
    return(tmpPool)

def scoreWord(word,wChar):
    tmpWord = ''
    score = 0
    for tmpChar in word:
        if tmpChar not in tmpWord:
            tmpWord = tmpWord + tmpChar
            if tmpChar in wChar:
                score += 1
            if tmpChar in 'etaionshr':
                score += 1
    return score

#guess = input("Enter your 5 letter word guess:")
#print (guess)

wCharDefault = 'qypfgjzxbn'
yCharDefault = '2u5s'
gCharDefault = '1s4l5k'

filename = "dictionary5.json"
with open(filename, 'r') as file:
    dict = json.load(file)
file.close

n = int(input("Your Wordle Round\n"))


wChar = 'abcdefghijklmnopqrstuvwxyz'
if n > 1:
    wChar= input("White Keys, like: "+ wChar +"\n")

yChar = {}
gChar = {}
pool = {}
confirmedChars = {}

for nQuard in range (1,5):
    yChar[nQuard] = ''
    gChar[nQuard] = ''

bSuccess = {}
for nQuard in range(1, 5):
    bSuccess[nQuard] = False

for k in range (n,10):
    newList = []
    for nQuard in range (1,5):
        if not bSuccess[nQuard]:
            if k > 1:
                yCharIn= input(str(nQuard) + ", Yellow Tiles, like: "+ yChar[nQuard] + "\n")
                gCharIn= input(str(nQuard) + ", Green Tiles, like: " + gChar[nQuard] + "\n")
            else:
                yCharIn = ''
                gCharIn = ''

            yChar[nQuard] = yChar[nQuard] + yCharIn
            gChar[nQuard] = gChar[nQuard] + gCharIn

            # print ('yChar', yChar[nQuard])
            # print ('gChar', gChar[nQuard])

            #if wChar == '':
            #    wChar = wCharDefault
            #if yChar == '':
            #    yChar = yCharDefault
            #if gChar == '':
            #    gChar = gCharDefault
            (pool[nQuard],confirmedChars[nQuard]) = formPool(wChar,yChar[nQuard],gChar[nQuard])

            # print(nQuard,pool[nQuard])
            # print (nQuard, confirmedChars[nQuard])

            if k > 1:
                print ("Guessing...")
                wordList = clue(pool[nQuard],confirmedChars[nQuard],dict)
                #dict = list2dict(wordList)
                nLen = len(wordList)
                print (nLen, "words found.")
                i=0
                tmpWord = {}
                for word in wordList:
                    i += 1
                    score = scoreWord(word,wChar)
                    if nLen <= 2:
                        score = 51 - nLen
                        print (word, score)
                    tmpWord = {"score": score,"guess":word}
                    newList.append(tmpWord)
    i=0
    for singleWord in sorted(newList,key = lambda  i:(-i['score'],i['guess'])):
        print(i,singleWord)
        i = i+1
        if i >= 10:
            break

    if k <= 9:
        guessWord = input ("Round " + str(k) +" Guess: \n")
        nSuccess = int(input("Is it the correct Guess? Enter 1, 2, 3 or 4 \n"))

        if nSuccess >= 1 and nSuccess <= 4:
            bSuccess[nSuccess] = True
        bSuccessCombined = True
        for nQuard in range (1,5):
           bSuccessCombined = bSuccessCombined and bSuccess[nQuard]

        if bSuccessCombined:
            break
        else:
            wChar = removeCharFromWChar(wChar,guessWord)
            # print(wChar)
