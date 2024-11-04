#LECTURE 5

#tuple are lits that are immodifiable
my_string = 'stefano'
my_list= ['one', 'two', 'three']
my_tuple = ('alpha', 'beta', 'gamma')

print(my_string[1])
print(my_list[1])
print(my_tuple[1])

#my_string[1] = 'a' #this will give an error
my_list[1] = 'four' #this will work fine
#my_tuple[1] = 'delta' #this will give an error

 #tuples are used to return multiple values from a function, they increase the readability of the code, inmodifiability is a feature, they are a sort of list 

my_tuple.index("three") #this will give an error
my_tuple.index("gamma") #this will work fine
print(my_tuple.index("gamma"))

#a tuple consumes less memory than a list (because it is immodifiable) (it is faster to access the elements of a tuple than the elements of a list beca
# because the elements of a tuple are stored in a contiguous block of memory, while the elements of a list are stored in different blocks of memory)
#(because it has fewer methods and functionalities than a list)

#it is a good solution when varaible is needed (no nees to edit the tuple content)



#sets
fruits {'apple', 'banana', 'orange'}        #this is a set
fruits.add('strawberry')    #this will add the element to the set

# nothing is done if the element is already in the set
fruits.remove('apple')   

#an item is dropped
fruits.remove('banana')  #this will give an error if the element is not in the set

if "peach" in fruit:
    fruits.remove('peach')
    
fruits.discard('peach')  #this will not give an error if the element is not in the set

print(fruits)

#how to drop duplicate items from lists
my_list = ['one', 'two', 'three', 'one', 'two', 'three']
my_set = list(set(my_list))
print(my_list)

#sets support basic set operations (union, intersection, difference, symmetric difference)
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {1, 2, 3, 5, 7}

print(odds.union(evens))
print(odds.union(odds))
print(odds.intersection(primes))
#A (odds) - B (primes)
print(evens.difference(primes))


















































































































































































