#lamba functions 
#map function
import csv
import sys
#lambda: anonymous function

#lambda arguments: expression    #syntax
def square(var):
    return var**2

square = lambda x: x**2

print(square(2))

#lambda function are useful when you want to apply an expression to a list od values 
#introduce the map function
# map (funct, items)  #syntax
nums_to_square = [1,2,3,4,5]
squared_nums = list(map(square, nums_to_square)) #map returns a map object, so we need to convert it to a list

#alrernatively
squared_nums = list(map(lambda x: x**2, nums_to_square)) #map returns a map object, so we need to convert it to a list
print(squared_nums)


#consider the supermarket daatsetof the last exercises
#each record contains the number of items that has been selled 
#i want to calculate the normalized qutility of sold items
#normalized quantity = quantity sold / total quantity sold  #normalized quantity is the percentage of the total quantity sold   
with open (r"C:/Users/memmo/OneDrive/Documenti/GitHub/MEMMOLA-s-REPOSITORY/Python/supermarket.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    records=list(reader)
records.pop (0)

print(records[0][1])
print(records[0][7])
branches = []
items=[]
for r in records:
    #new branch
    if r[1] not in branches:
        branches.append(r[1])
        try:                                    #try and except are used to manage the exception, in case the value is not a number 
            branch_quantities = [int(r[7])]
        except:
            branch_quantities = [0]
        items.append(branch_quantities)
    else:
        #the branch is already in the list
        branch_index = branches.index(r[1])
        items[branch_index].append(r[7])
        
for b, i in zip(branches, items):
    s= sum(i)
    print(f"The branck {b} sold {s}.")


print (items[0])
#normalized quantity = quantity sold / total quantity sold  #normalized quantity is the percentage of the total quantity sold
#normalaze the ste series of the values for each branch
normalized_items = []
for i in items:
    min_value = min(i)
    max_value = max(i)
    normalized_items.append(list(map(lambda x: (x - min_value) / (max_value - min_value),2, i))) #lambda function to normalize the values

print (normalized_items[0])

sys.exit()

