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
for i in items:
    print(i)

# what is the output of this command?
print(list(range(len(items))))

# list sorting
print(items)
items.sort()
print(items)

# discover how sorting is performed in Python
# have a look at the quicksort, mergesort
# exercise: try to implement quicksort as a custum function

# list slicing
# list of dwarfs
dwarfs = ["Doc", "Bashful", " Grumpy", "Sneezy", "Happy", "Sleepy", "Dopey"]
print(dwarfs)
print(dwarfs[1:5])
print(dwarfs[:5])
print(dwarfs[5:])
print(dwarfs[:5] + dwarfs[5:])
print(dwarfs[:])
print(dwarfs[1:5])
print(dwarfs[1:5:2])
print(dwarfs[-1])
print(dwarfs[-5:-1])
print(dwarfs[-1:-5:-1])
print(dwarfs[::-1])

# exercise: given a list, reverse the left with the right part
# (calculate the middle index, and then use slicing to reverse)

# list of lists
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(A)
print(A[1])
print(A[1][2])
print(A[0][-1])
# get the items of the last column
last_column = []
for item in A:
    # get the last item of the row
    last_column.append(item[-1])

# same with list comprehension
last_column = [row[-1] for row in A]
print(last_column)

sys.exit()
