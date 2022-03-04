# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import GuessWord
import json

filename = "dictionary5.json"
with open(filename, 'r') as file:
    dict5 = json.load(file)
file.close

print(dict5)
strGame = input("What game do you want to play? Enter 'w' for Wordle. 'q' for Quardle.").lower()
if strGame == 'q':
    totGames = 4
    totRounds = 9
    strGame = "Quardle"
else:
    totGames = 1
    totRounds = 6
    strGame = "Wordle"


bSuccess = GuessWord.guessWord(totGames,totRounds,strGame,dict5)

if bSuccess:
    print ("Congrats!")
else:
    print ("Better luck next time!")