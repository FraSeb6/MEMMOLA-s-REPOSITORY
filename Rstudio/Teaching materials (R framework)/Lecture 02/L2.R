install.packages("mclust", dependencies = TRUE)

library("mclust")
data("diabetes")
head(diabetes)

x <- 14.33 ### assign a decimal value
class(x)  ### class of x    Decimal values are called “numeric” in R.
#It is the default computational data type.

#If a decimal value is assigned to a variable x, x will be of numeric type

typeof(x)  ### type of R object of x

#Even if an integer is assigned to a variable x, it is still numeric:
x <- 10 ### assign an integer value
is.integer(x) ### is x an integer?

#To create an integer variable, as.integer() can be invoked:
x <- as.integer(11) ### assign an integer data type
is.integer(x)       ### is x an integer?

#Integers can also be declared by appending an L suffix:
y <- 22L       ### assign an integer data type
is.integer(y)  ### is y an integer?

#complex number
z <- 5+2i  ### assign a complex number
typeof(z)   ### class of z
#Basic functions supporting complex arithmetic are:
Re(z)    ### real part
Im(z)    ### imaginary part
Mod(z)   ### modulus

#A logical value is often created via comparison between variables:
x <- 2 > 1    ### is 2 greater than 1?
x

#Standard logical operations are & (and), | (or), and ! (not):
u <- TRUE
v <- FALSE
u & v

#A character object is used to represent string values in R. 
#Two character values can be concatenated with the paste function:
address <- 'Via'
domain <- 'Conservatorio'
paste(address, domain, sep = ' ')

#To substitute terms in a string use sub():
my_str = "Via Conservatorio"
sub("Via", "Piazza", my_str)
#More functions for string manipulation can be found in the R documentation using ?sub.
#A very convenient package to work with strings is stringr
  
#     Basic data structures

# Vectors

#The basic data structure in R is the vector. 
#Vectors are usually created with the c() function, short for “concatenate”:
c(1,2,4,8,16,32)
c("Italy","Spain","France","UK","Ireland","Belgium")
#Vectors can contain only equal data types. If this is not the case, some conversion takes place:
c(FALSE,1,"2")
#In this case FALSE and 1 will be converted to characters
#These are vectors with attached labels:
c('Tottenham' = 14, 'Aston Villa' = 12, 'Brentford' = 6)
#You can also use names():
x <- c(14,12,6)  ### vector
n <- c('Tottenham','Aston Villa','Brentford')    ### vector of names
names(x) <- n    ### assigning names
x
#In R, a matrix is a collection of similar data types arranged in a two-dimensional rectangular layout. 
#They are usually created with the matrix() function:
matrix(data = c(1,2,3,5,8,13), ### the data elements (First Fibonacci numbers)
       ncol = 3,              ### number of columns
       nrow = 2,              ### number of rows
       byrow = TRUE)          ### fill matrix by rows
#As for named vectors, named matrices can contain labels to be attached to rows and/or columns:
### Generating a named matrix
M <- matrix(data = c(1,2,3,5,8,13), ### the data elements (First Fibonacci numbers)
            ncol = 3,              ### number of columns
            nrow = 2,              ### number of rows
            byrow = TRUE)          ### fill matrix by rows
rn <- c('r1','r2')       ### vector of rownames
cn <- c('c1','c2','c3')  ### vector of colnames
rownames(M) <- rn        ### assign rownames
colnames(M) <- cn        ### assign colnames
M
#   list
#A collection of objects (numbers, vectors, matrices, etc.). Lists are the most general 
#and flexible elements in R because they can contain elements of any type (including other lists).
new_list <- list(
  A = matrix(c(4, 1, 1, 8), ncol = 2),
  y = c(1, 2, 6, 6, 9)
)

new_list
#   data frame
# A class of objects to represent data matrices.
# The rows correspond to statistical units (i.e., observations)
# The columns correspond to variables.
head(iris,n = 10)
#NB: Internally, an object of class data.frame is saved 
#as a list whose elements all have the same length and, typically, a name.
str(iris)
#New data frames are usually created with the data.frame() function.
#Beware: data.frame()’s default behaviour turns strings into factors

#   Little detour: factors
# Factors - Definition
#They are used to represent categorical data and can be either ordinal (e.g., company hierarchies) 
#or non-ordinal (e.g., hair color).
#A factor MUST be imagined as a vector of integers, where each integer is associated with a label.
#Let’s try to create our first factor:
x <- factor(c("yes", "yes", "no"))
x
#The order in which the levels are represented can be modified using the levels 
#argument of the factor function. By default, the levels are ordered alphabetically.
#Additionally, if the levels have a hierarchy (e.g., soldier, lieutenant, marshal, etc.), 
#we can indicate this by specifying ordered = TRUE in the factor function.

#Given a factor, we can use the table function to obtain a table 
#with the levels and frequencies of the variable.
x <- factor(c("A", "B", "A", "B"))
x  # printing the factor
str(x)  # structure of the factor
table(x)  # table with levels and frequencies
#Never forget that a factor is nothing more than an integer associated with a label.
x <- factor("a")
y <- factor("b")
c(x, y)
#A very convenient package to work with factors is forcats
#To avoid the problem of converting strings into factors, 
#use stringsAsFactors = FALSE when creating data frames
v1 <- c(10,20,30)                                ### numeric vector
v2 <- c('a','b','c')                             ### character vector
v3 <- c(TRUE,TRUE,FALSE)                         ### logical vector
data.frame(v1, v2, v3, stringsAsFactors = FALSE) ### data.frame
#A more modern-like data.frame object is a tibble from the tibble package

#   Subsetting Data Structures (1)
# Subsetting Vectors
#Values in a vector are retrieved by using the single square bracket [] operator:
s = c("a"=5, "b"=4, "c"=3, "d"=2, "e"=1)
s[3]
#You can also drop elements from a vector with -
## drop the 3rd element
s[-3]
## out-of-range index returns NA
s[10]
#You can also retrieve more than one element:
indx <- c(2, 3, 5, 5)
s[indx]
#You can drop more than one element from a vector with -
indx <- c(1, 3)
s[-indx]
#You can also retrieve elements with their names:
i_names <- c('d', 'b')
s[i_names]
#You can also use logical vectors to retrieve values:
i_logical <- c(FALSE, FALSE, TRUE, FALSE, FALSE)
s[i_logical]
#We can also use conditional subsetting:
## select elements greater than 2
i <- s > 2
s[i]
#Values in a matrix are retrieved by using the [,] operator, 
#placing the row and column dimension before and after the comma:
M <- matrix(1:12, nrow = 3, ncol = 4, byrow = TRUE)
rownames(M) <- c('r1', 'r2', 'r3')
colnames(M) <- c('c1', 'c2', 'c3', 'c4')
M ## print the full matrix
M[2, 3]
#You can also retrieve an entire row or column:
M[1, ]
M[,1]
i <- c(2, 3)
M[i, ]
M[c(1, 3), c(2, 4)]
#We can use names of columns and rows:
i <- c('r1', 'r3')
M[i, ]
i <- c('c2', 'c4')
M[, i]
i <- c('c2', 'c4')
M[3, i]
#We can also use logical vectors:
i <- c(TRUE, FALSE, FALSE)
M[i, ]
i <- c(TRUE, FALSE)  ## ->  c(TRUE, FALSE, TRUE)
M[i, ]
i <- M[, 'c3'] < 2 * M[, 'c1']
M[i, 'c4']
#Slightly different from vectors. In particular:
new_list[2]
str(new_list[2]) # A LIST containing only the second element
new_list[[2]]
str(new_list[[2]]) # the second element of the list
#We can extract elements using $
new_list$A
new_list[["A"]]
#Being lists, extracting one or more columns works as usual
head(iris$Sepal.Length) # output: vector
head(iris[["Sepal.Length"]]) # output: vector
head(iris[[1]]) # output: vector
head(iris[1]) # output: dataframe with 1 column named Sepal.Length
#In addition, R allows to use a typical matrix syntax
iris[1, ] # the first row
head(iris[, 1]) # the first column (as a numerica vector)
iris[1, 3] # the observation corresponding to the first row and the third column
head(iris[, 1,drop=FALSE],n = 3) # the first column (as a one-dimensional data frame)

