# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
                            bWord = isWord(word, dictionary)
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

def inChar (msg,myChar):
    tmpChar = input(msg)
    tmpLen = len(tmpChar)
    if tmpLen > 0:
        if tmpChar[0].isnumeric() or tmpChar[0] == 'z':
            if tmpChar[0:2] == 'zz':
                if tmpLen > 2:
                    myChar = tmpChar[2-len(tmpChar):]
                else:
                    myChar = ''
            else:
                myChar = myChar + tmpChar
            return (myChar)
        else:
            return(myChar)
    else:
        return(myChar)

def guessWord(totGames,totRounds,dict5):
    wCharDefault = 'qypfgjzxbn'
    yCharDefault = '2u5s'
    gCharDefault = '1s4l5k'


    n = int(input("Your Quordle Round\n"))

    wChar = 'abcdefghijklmnopqrstuvwxyz'
    if n > 1:
        wChar = input("White Keys, like: "+ wChar +"\n")

    yChar = {}
    gChar = {}
    pool = {}
    confirmedChars = {}

    for nQuard in range (1,totGames + 1):
        yChar[nQuard] = ''
        gChar[nQuard] = ''

    bSuccess = {}
    for nQuard in range(1, totGames + 1):
        bSuccess[nQuard] = False

    for k in range (n,totRounds + 1):
        newList = []
        for nQuard in range (1,totGames + 1):
            if not bSuccess[nQuard]:
                if k > 1:
                    msg = str(nQuard) + ", Yellow Tiles, like, " + yChar[nQuard] + ":"
                    yCharIn = inChar(msg, yChar[nQuard])
                    msg = str(nQuard) + ", Green Tiles, like, " + gChar[nQuard] + ":"
                    gCharIn = inChar(msg, gChar[nQuard])
                else:
                    yCharIn = ''
                    gCharIn = ''
                yChar[nQuard] = yCharIn
                gChar[nQuard] = gCharIn

                #print('yChar', yChar[nQuard])
                #print('gChar', gChar[nQuard])

                #if wChar == '':
                #    wChar = wCharDefault
                #if yChar == '':
                #    yChar = yCharDefault
                #if gChar == '':
                #    gChar = gCharDefault
                (pool[nQuard],confirmedChars[nQuard]) = formPool(wChar,yChar[nQuard],gChar[nQuard])

                # print(k, nQuard,pool[nQuard])
                # print(k, nQuard, confirmedChars[nQuard])

        for nQuard in range(1, totGames + 1):
            if not bSuccess[nQuard]:
                if k > 1:
                    # print(pool[nQuard])
                    # print(confirmedChars[nQuard])
                    bGuess = True
                    for n in range(1,nQuard):
                        if pool[n] == pool[nQuard] and confirmedChars[n] == confirmedChars[nQuard]:
                            bGuess = False
                            wordList = []
                            break
                    if bGuess:
                        print("Guessing " + str(nQuard) + "...")
                        wordList = clue(pool[nQuard],confirmedChars[nQuard],dict5)
                        #dict5 = list2dict(wordList)
                        nLen = len(wordList)
                        print (nLen, "words found.")
                    i=0
                    tmpWord = {}
                    for word in wordList:
                        i += 1
                        score = scoreWord(word,wChar)
                        if nLen <= 2:
                            score = 51 - nLen
                            # print (word, score)
                        tmpWord = {"score": score,"guess":word}
                        newList.append(tmpWord)
        i=0
        for singleWord in sorted(newList,key = lambda  i:(-i['score'],i['guess'])):
            print(i+1,singleWord["guess"], singleWord["score"])
            i = i+1
            if i >= 5:
                break

        if k <= totRounds:
            guessWord = input ("Round " + str(k) +" Guess: ")
            nSuccess = int(input("Is it the correct Guess? Enter 1, 2, 3 or 4."))

            if nSuccess >= 1 and nSuccess <= 4:
                bSuccess[nSuccess] = True
            bSuccessCombined = True
            for nQuard in range (1,totGames + 1):
               bSuccessCombined = bSuccessCombined and bSuccess[nQuard]

            if bSuccessCombined:
                break
            else:
                wChar = removeCharFromWChar(wChar,guessWord)
                # print(wChar)
    return(bSuccessCombined)