import sys
import csv


        
#use of list
items = list([1, 2, 3, 4, 5])
print (items)
items= ['summer', 'autumn', 'winter']
len(items)
print(items[0])

items.append('spring')
print(len(items))

#iterate over the list 
for i in items:
    print(i)
    
#what is the output of this command 
print (list(range(len(items)))) 

#list sorting
print (items)
items.sort()
print(items)

#discover how sorting is performed in Python
#have a look at the quicksort, mergesort
#excise 

#list slicing
#list of dwarfd
dwarfs =['Doc', 'Bashful', 'Grumpy', 'Sneezy', 'Happy', 'Sleepy', 'Dopey']
print(dwarfs[1:5])
print(dwarfs[:5])
print(dwarfs[5:])
print(dwarfs[:5]+ dwarfs[5:])
print(dwarfs[:])
print(dwarfs[1:5:2])
print(dwarfs[-1])
print(dwarfs[-5:-1])
print(dwarfs[-1:-5:-1])# we start from the last element of the list ae we red from -1 to -5
print(dwarfs[::-1])
#same syntax of the string
#futher exrcise: given a list, reverse the left eith the right art (calculate the middle index, and then use slicing to reverse)


#list of list
A=[[1,2,3],[4,5,6],[7,8,9]]
print (A)
print(A[1])#remember python stars to count from zero
print (A[1][2])#the second square bracket selects the element present in the selected bracket by indicating the first bracket
print(A[0][-1])

#
#this two scripts do the same task
last_colums=[]
for item in A:
    #get the last item of the row
    last_colums.append(item[-1])  #more redundant of the following  
#in this case if A contains anything and the for doesn't excute, but still this cose would print out the list last column, as an empty one

column = [row[2] for row in A]
# another way of writing a loop, scrolls over the items of A, and for each element it takes the last element of th erow (of each list within the list in our case) 
print (last_colums)

#letsgonsky do it in a real example
#read a file and process the rows as list items

#open the file and read the content 
with open ('dataset/supermarket.csv', newline=",") as f:
    reader = csv.reader(f, delimiter=',')
    records =list(reader)
print(records)
#if the file is in the same folder as the one you are currently in then it will run currently
#if not not it will return an error, then to run it correctly you'll have to refer to the right folder in which the data is located by starting
#for instnce open ('dataset/supermarket.csv', newlines="")if the data you want to use in located in that folder
print(records [0]) 
#the first row might reult being the header of our table/matrix
#how can we replace with the content of rows from the second row, wanting to pull 

#how can i replace records with the content of rows from the second row, wating to pull of the first row since it's the header
record = records[1:]

def unique_values(my_list):
    #we use lopps
    values=[]
    for item in my_list:
        if item not in values:
            values.append(item)
    return values        

def unique_values_by_set(my_list):
    my_set = set(my_list)
    return list (my_set)



#create a list with the unique names of branches 
branches= [row[1] for row in records]
#print[branches]
unique_branches = unique_values(branches)
print (unique_branches)
# build a list of sales by branch
# build a list  of lits where each row is about a branch
# each row contains a list of sales of the given branch
# sales = [ [ 123, 45345, 2342], [2342,2352, 23525, 24234], [2342,3453, 34535] ]
sales =[]
#try to find a solution, discussion in the next class






sys.exit()
