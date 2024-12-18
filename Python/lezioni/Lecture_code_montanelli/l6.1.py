# we want to implement the Wordle game
# https://www.nytimes.com/games/wordle/index.html

# you have X attempts to guess the target word that is randomly selected within the 5-letter words in English

# rules:
## A correct letter turns green
## A correct letter in the wrong place turns yellow
## An incorrect letter turns gray

# for any attempt, the feedback must report green-yellow-gray letters
# use tiles to provide a feedback (see the pic in the attachment)


# cases to handle (with a message to the player)
# words that are not in the dictionary
# words with length different from 5
# words already guessed (do not consume tries, we need a history)

import sys
import csv
from random import choice
from termcolor import colored

# setup
max_attempts = 6
tiles = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬛"}

#check_guess returns colored tiles and the tiles that are the feedback on a letter-by-letter comaparison of guess and target
def check_guess(guess, target):
    global tiles
    colored_letters= []
    tiles= []
    for i in enumerate(guess, target):
        if guess[i] == target[i]:
           #color in green
           colored_letters.append(colored("green", guess[i]))
           colored_tiles.apped(tiles ["correct_place"])
        elif guess[i] in target:
            #color in yellow
            colored_letters.append(colored("yellow", guess[i]))
            colored_tiles.append(tiles["correct_letter"])
        else:
            #color in gray
            colored_letters.append( guess[i])
            colored_tiles.append(tiles["incorrect"])
            
    print(colored_letters)
    print("".join(colored_tiles))
    return "".join(colored_letters), "".(colored_tiles)       
       
# main
# load the EN dictionary and isolate the 5-letter words
with open("dataset/en_unigram_freq.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

records.pop(0)
# print(records[0])

# drop the frequencies
# [f(x) for x in iterable]
en_words = [x[0] for x in records]
# print(en_words)

# limit to 5 letter-words and switch to uppercase
# [f(x) for x in iterable if condition]
en_words_5 = [x.upper() for x in en_words if len(x) == 5]
# print(en_words_5[100:106])
# print(len(en_words_5))

# pick-up the target
# more sophisticated methods for choosing the target are possible
# consider random.choices that allows to consider weights associated with words
# the word frequencies could be used to make more probable the words that are less frequent
# this way, it is possible to define the game difficulty
target = choice(en_words_5)

print("Welcome to WORDLE!")
print(f"Guess the target word, you have {max_attempts} tries.")

#list of attempts
history= []
colored_tiles=[]

attempt= 1

#while loops consider the nuber of attempts (that needs to be  lower than the maximum)
while attempt <= max_attempts:
    #enter the guess
    guess= input(f"Insert a 5-letter word: ").upper()
    except KeyboardInterrupt:
    if guess == target:
        #prin   is green the letters nd then go
        print("good job! the target is gussed!")
        break
    
    #check possible errors in the attempt:
    #not in dict; not 5 letters; consider the history
    if len(guess) != 5:
        print("The word must have 5 letters, try again")
        continue
    elif not guess.isalpha():
        print("Please; insert a word in the English dictionary")
        continue
    elif geuss in history:
        print("The duess is already tried; guess another one!")
        continue
    elif guess not in en_words_5:
        print("Please; insert a word in the English dictionary")
        continue
    else:
        #if the guess is the target or provide a feedback
        #increse the number of attemptsù
        history.append(guess)
        colored, titles =check_guess(guess, target)
        colored_titles.append(colored)
        colored_titles.append(tiles)
        attempt += 1
    
    
    if guess in history:
        print("You already guessed this word, try again")
        continue
    if guess not in en_words_5:
        print("This word is not in the dictionary, try again")
        continue
    history.append(guess)
    #work on your solution, discussion in the next classes
    attempt += 1   
    #if the guess is the target or provide a feedback
    
    if guess in history:
        print("You already guessed this word, try again")
        continue
    if guess not in en_words_5:
        print("This word is not in the dictionary, try again")
        continue
    history.append(guess)
    #work on your solution, discussion in the next classes
    attempt += 1
#enter the guess

#check possible errors in the attempt:

# work on your solution, discussion in the next classes

sys.exit()
