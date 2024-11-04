import re
import string
#list
#list is a collection of items, it can be of any type, and it can be looped item by item


#focus on dictionaries
capitals = {
    'Italy': 'Rome',
    'France': 'Paris',
    'Germany': 'Berlin'
    }
#lists are arrays 
#dictionaries are associative arreys you can associate a key to an item. they can be of any type, and they can be looped item by item
#the list can contains only one element fo each key (item) o(only countries or cities)
print(capitals['Italy'])
#print(capitals.keys[])
#print(capitals.values[]) #in this way yoou can print the values into two different lists
#list-version of the dictionary
capitals["spain"] = "Madrid"
#use get ()
#print(capitals.get('Italy'))


#if 'Austria'in capitals:
   # print('Austria is in the dictionary')   
#else:    
 #   print('Austria is not in the dictionary')  

 
capitals_list = [  
                 'Rome',
                 'Paris',
                 'Berlin'
                 ]

#print (capital_list[0]) #print Rome

#count the occurences of a word in a text
#read in memory the content of the rtext from file
open('C:/Users/memmo/OneDrive/Desktop/python/supermarke.csv', 'r', encoding='utf-8')
my_text = my_file.read()
print(my_text)
#drop the punctuatio
# nmethod 1.list comprehension
cleaned_text = [char for char in my_text if char not in string.punctuation]
cleaned_text = ''.join(cleaned_text) #join the list of characters into a string 
print(cleaned_text)
#method 2. regular expressions
#\s any whitespace, newline, newtab
#\w any alphanumeric character including letters and numbers
cleaned_text = re.sub(r"[^\w\s]", "", my_text)
print (cleaned_text)
# reduce the capitalization

#split words
