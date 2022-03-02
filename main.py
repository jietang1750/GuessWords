# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import GuessWord
import json

totGames = 1
totRounds = 6

filename = "dictionary5.json"
with open(filename, 'r') as file:
    dict5 = json.load(file)
file.close

print(dict5)

bSuccess = GuessWord.guessWord(totGames,totRounds,dict5)

if bSuccess:
    print ("Congrats!")
else:
    print ("Better luck next time!")