# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import enchant
import json
import time

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

def isWord(strWord,dict):
    return(dict.check(strWord))


#Load English dictionary
dict = enchant.Dict("en_US")

#guess = input("Enter your 5 letter word guess:")
#print (guess)

pool1="abcdefghijklmnopqrstuvwxyz"
pool2="abcdefghijklmnopqrstuvwxyz"
pool3="abcdefghijklmnopqrstuvwxyz"
pool4="abcdefghijklmnopqrstuvwxyz"
pool5="abcdefghijklmnopqrstuvwxyz"

confirmedChars = ""

word = ''
wordList=[]
wordDict={}
i=0
for i1  in range (0,len(pool1)):
    word1=pool1[i1]
    #print("1",i1,word)
    for i2 in range (0,len(pool2)):
        word2 = word1 + pool2[i2]
        #print("2", i2, word)
        for i3 in range(0, len(pool3)):
            word3 = word2 + pool3[i3]
            #print("3", i3, word)
            for i4 in range(0, len(pool4)):
                word4 = word3 + pool4[i4]
                #print("4", i4, word)
                for i5 in range(0, len(pool5)):

                    word5 = word4 + pool5[i5]
                    word = word5

                    bConfirm = True
                    for k in range (0,len(confirmedChars)):
                        tmpChar = confirmedChars[k]
                        if (tmpChar not in word) and bConfirm:
                            bConfirm = False
                            #print("no", i1, i2, i3, i4, i5, word)
                            break
                    if bConfirm:
                        bWord = isWord(word,dict)
                        #print("yes", i1, i2, i3, i4, i5, word)
                        #print(wordList,word)
                        if bWord:
                            # print(i1,i2,i3,i4,i5, word)
                            wordList.append(word)
                            i += 1
                            if word[0] not in wordDict.keys():
                                wordDict[word[0]]=[]
                            wordDict[word[0]].append(word)
                            #print (i, word, end = '\r')
                            print (i, word)

filename = 'dictionary5.json'
with open(filename, 'w') as file:
    json.dump(wordDict, file)
file.close()

filename = 'wordlist.json'
with open(filename, 'w') as file:
    json.dump(wordList, file)
file.close()
