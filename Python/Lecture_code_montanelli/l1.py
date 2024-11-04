"""This is the intro to Python programming"""

""" Python in an interpretative language, which means that it is executed line by line, unless it's written differently by the semantics of the program.
    this means if there is an error in the code, the program will stop at the line where the error is found.
    
    Python is an object-oriented language, which means that it uses objects to represent data and methods to manipulate the data.
    Python is case sensitive.
    Python uses indentation to define code blocks.
    (the other type is compiled language, which is executed after the whole code is compiled)
"""
"""'=' is used to assign a value to a variable, 
    use underscores _, to separate words in variable names
    don't use uppercase
    it can't have blank spaces in the name
"""

"""A  'variable' is a container for storing data values.
    Python has no command for declaring a variable.
    A variable is created the moment you first assign a value to it.
    - Variables do not need to be declared with any particular type and can even change type after they have been set.
    - Variables can be declared by any name or even a single letter, but it is recommended to use meaningful names to the variables.
    - If we create a variable without assigning a value to it, it will have a value of None.
    - if we create a variable with the same name of an old one in the program, the old one will be overwritten.
"""

"""A 'string' is a sequence of characters, enclosed in single or double quotes.
    - Strings can be assigned to variables. 
"""
print("Hello, 'World'!")  # this is a string, in this case you can inlude the ' ' inside the ""
print('Hello, World!')  #this is a string, in this case you can inlude the " " in the string itself 
print("Hello, \"World\"!")  # this is a string, in this case you can inlude the " " inside the ""

"""print() is a built-in function in Python, it is used to print the specified message to the screen."""

import sys

# return the result of an exam according to the result of different modules
# consider that modules can be weighted
# consider to manage courses with a non-predefined number of modules

# setup for three fixed modules
m1_grade = 18
m2_grade = 20
m3_grade = 30

m1_weight = 0.25
m2_weight = 0.25
m3_weight = 0.5

# setup for a variable number of modules as a list
"""then in our file we wanted the number of modules to be free and dynamic, in order not to b constrained to a strict number of modules. 
    To do this we used lists, which are a collection of items, that can be of different types, and can be changed after they are created."""
#considering a dynamic number of modules
grades = [18, 20, 30, 25]
weights = [0.25, 0.25, 0.5, 1]
#we need to iterate over the grades and weights lists to calculate the final grade
sum_modules = 0
for i, num in enumerate(grades):
    sum_modules += num * weights[i]
grade = sum_modules / sum(weights)
"""enumerate() is a built-in function that returns an enumerate object. 
    - It contains the index and value of all the items in the list as pairs.
    - is a function that returns an enumerate object, the elements of list one by one enumerate will return a list within which each element is composed by two things: 
        - the index 
        - the value of the element.
    then creating  an iteration with enumerate, we are iterating through two elements each time
"""

################# in order to understand better what enumerate creates:

my_list = ['apple', 'banana', 'cherry']

# Using enumerate to create an indexed list
enumerated_list = list(enumerate(my_list))

# Printing the enumerated list
print(enumerated_list)

""" 
    the printed result is the following: 
    [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
"""



# grade with three modules
# grade = (m1_grade + m2_grade + m3_grade) / 3

# grade with three weighted modules
# grade = (m1_grade*m1_weight + m2_grade*m2_weight + m3_grade*m3_weight) / (m1_weight + m2_weight + m3_weight)

# grade with lists
# iterate/loop over the grades/weights lists
sum_modules = 0
# for i, num in enumerate(grades):
#    sum_modules += num * weights[i]

# solution based on iteration over lists with zip
sum_modules = sum([a * b for a, b in zip(grades, weights)])

grade = sum_modules / sum(weights)

if grade >= 18:
    print("exam passed")
else:
    print("exam failed")
"""in python identation is crucial, it is used to define code blocks, and it is recommended to use 4 spaces for identation."""



"""
    Though we could do it differently in Python:
"""
#instead of the for loop we can calculate sum_modules
sum_modules = sum([a*b for a,b in zip(grades, weights)]) 
#zip() is a built-in function that returns an iterator of tuples, where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.

#in otder to understand better what zip does:
wow= list(zip(grades, weights))
print('stampa funzione zip', wow)

""""
    [(18, 0.25), (20, 0.25), (30, 0.5), (25, 1)]
"""
#we create a list of tuples, where each tuple is composed by the elements of the two lists at the same index

"""The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
    and then the second item in each passed iterator are paired together etc.
"""

"""
    zip() is a built-in function that returns an iterator of tuples, where the first item in each passed iterator is paired together, 
    and then the second item in each passed iterator are paired together etc.
        - The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
        - The zip() function returns an iterator of tuples based on the iterable objects.
        - If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
        - The zip() function can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
        - The zip() function returns an iterator of tuples where the first item in each passed iterator is paired together, 
        and then the second item in each passed iterator are paired together etc.
"""




"""
    A tuple is a data structure in Python that stores an ordered, immutable collection of items. 
    Each item in a tuple can be of any data type, and you can access elements by their position (index), similar to a list. 
    However, unlike lists, tuples cannot be modified after they are created, which means you cannot add, remove, or change elements in a tuple.7
    
        - Immutable: Once created, the elements in a tuple cannot be changed, which makes tuples a safe choice when you want to ensure data remains constant throughout your program.
        - Ordered: The elements have a defined order, and this order will not change unless the tuple itself is modified (which can only happen by creating a new tuple).
        - Allow Duplicates: Like lists, tuples can contain duplicate values.
        
    Why Use Tuples?
    
        - Data Integrity: Since tuples are immutable, they’re useful for storing data that shouldn't change.
        - Performance: Tuples are generally faster than lists due to their immutability.
        - Hashable: Because tuples are immutable, they can be used as keys in dictionaries (unlike lists).
"""

sys.exit()