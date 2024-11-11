import sys

# use of lists
items = [1, 2, 3, 4, 5, 6]          # list of integers, created with the square brackets []
# alternative syntax
items = list((1, 2, 3, 4, 5, 6))    # list of integers, created from a tuple with the list() function
print(items)

# example with strings
items = ["summer", "autumn", "winter"]
print(len(items))                   # length of the list     
print(items[0])                     # access the first element

items.append("spring")              # add an element at the end of the list   
print(len(items))
"""
A list can contain any type of character: strings or integers

    In the last code we printed the length (function `len()` returning the length of an object) of the list ‘items’ 
    and the first item ([0])of the list, 
    and then we added a new element to the list (`’spring’`)

"""

# iterate over the list
for i in items:                    # iterate over the list, i is the variable that will contain the current item
    print(i)

"""
we can go through all the elements of a list using a for loop like the one above.
We can also use the function list() in order to create a list
Then we also may use the function range(), used to generate a sequence of numbers. It is commonly used in loops for iterating a specific number of times.
"""

# what is the output of this command?
print(list(range(len(items))))
"""     this code returns a list, and each element of the list is 0 to the length of the list
	    range(len(items)): The range(4) generates the sequence of indices [0, 1, 2, 3].
"""

# list sorting, it orders the list
print(items)
items.sort()
print(items)
"""
    this code first returns the list items not sorted and the second print, prints the list sorted as we asked 
"""

# discover how sorting is performed in Python
# have a look at the quicksort, mergesort
# exercise: try to implement quicksort as a custum function

# list slicing
# list of dwarfs
dwarfs = ["Doc", "Bashful", " Grumpy", "Sneezy", "Happy", "Sleepy", "Dopey"]
print(dwarfs)
print("reult of dwarfs[1:5]",dwarfs[1:5])                               # from the second to the fifth elementexcluded
print("reult of dwarfs[:5]",dwarfs[:5])                                 # from the first to the fifth element
print("reult of dwarfs[5:]",dwarfs[5:])                                 # from the sixth to the last element
print("reult of dwarfs[:5] + dwarfs[5:]",dwarfs[:5] + dwarfs[5:])       # concatenation of two lists, the result is the original list
print("reult of dwarfs[:]",dwarfs[:])                                   # copy of the list
print("reult of dwarfs[1:5]",dwarfs[1:5])                               # from the second to the fifth element
print("reult of dwarfs[1:5:2]",dwarfs[1:5:2])                           # from the second to the fifth element, with a step of 2
print("reult of dwarfs[-1]",dwarfs[-1])                                 # last element
print("reult of dwarfs[-5:-1]",dwarfs[-5:-1])                           # from the fifth to the last element
print("reult of dwarfs[-1:-5:-1]",dwarfs[-1:-5:-1])                     # from the last to the fifth element, with a step of -1
print("reult of dwarfs[::-1]",dwarfs[::-1])                             # reverse the list

# exercise: given a list, reverse the left with the right part
# (calculate the middle index, and then use slicing to reverse)

######### list of lists #########
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
    In this case the items of the list A are three, but each item is a list itself.
    A is a matrix
"""
print(A)            # print the matrix
print(A[1])         # print the second row of the matrix
"""
    the fist [] refers to the row, and the second [] to the column 
"""
print(A[1][2])      # print the third element of the second row
print(A[0][-1])     # print the last element of the first row


# get the items of the last column
last_column = []
for item in A:
    # get the last item of the row
    last_column.append(item[-1]) 
    print(last_column)
"""
    we can get the last column of the matrix A by iterating over the rows of the matrix and appending the last element of each row to a new list
"""
# same with list comprehension
last_column = [row[-1] for row in A]
print(last_column)
"""
    a syntetic way of writing a loop
    scrolls over the items of A, and for each element it takes the last element of the row (of each list within the list in our case) 
"""

sys.exit()
