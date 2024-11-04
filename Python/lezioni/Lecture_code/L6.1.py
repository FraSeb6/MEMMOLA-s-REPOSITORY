#world game 

#you have X attempts to guess the targhet word that is randmly selected whitin the 5-letter words in English

#need to manage
#words that are not in the dictionary
#words with length different from 5
#words already guessed (do not count as attempts)


import sys
import csv
from random import choise

#load the EN dictionary and isolate the 5-letter words
with open("C:/Users/memmo/OneDrive/Documenti/GitHub/MEMMOLA-s-REPOSITORY/Python/en_unigram_freaquency.csv", newline="", encoding="utf-8") as csvfile:
    records = list(csv.reader(csvfile, delimiter=","))
    records.pop(0)
    #print (records[0]) 

#drop the frequencies
en_words = []
print (records[0])
#drop the frequencies
en_words = [x[0] for x in records]
print (en_words[0])
#limit to 5-letter words and switch to uppercase
en_words_5 = [word.upper() for word in en_words if len(word) == 5]
print (en_words[0])

#select a random word
#check also the version with choise
target = choice(en_words_5)




sys.exit()  