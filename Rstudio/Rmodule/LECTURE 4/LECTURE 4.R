M <- matrix(1:20, ncol = 5, nrow = 4, byrow = TRUE)
print(apply(M, MARGIN = 2, FUN = mean)) ## Compute the mean of each column

apply(M, MARGIN = 2, FUN = mean)## Compute the mean of each column
colMeans(M)#do the same thins of print but it works only for mean  function not for other function

print(apply(M, MARGIN = 1, FUN = mean)) ## Compute the mean of each row

apply(M, MARGIN = 1, FUN = var)

x <- c(rnorm(10), runif(10), rnorm(10, 1)) 
f <- gl(3, 10)
tapply(X = x, INDEX = f, FUN = mean)

## X and INDEX need to have the same lenght
tapply(X = iris$Sepal.Length, INDEX = iris$Species, FUN = mean)


##----- attch funciont (don't use that is EVILLLLLLL)
tapply(X = iris$Sepal.Length, INDEX = iris$Species, FUN = mean)
Sepal.LEngth
attach(iris)
Species
# it change the environment, and it doesn't appear in the environment
#better with function
with(data=iris, tapply(X=Sepal.Length, INDEX =Species, FUN=mean))


sum_int <- function(n) {
  s <- sum(1:n)
  return(s)
}
sum_int(n = 100) #the output value (not mandatory)





norm_p <- function(x, p = 2) {
  d <- sum(x^p)^(1/p)
  return(d)
}
print(norm_p(x = c(1, 1)))      ## Compute the Euclidean norm of the vector c(1,1)


#the function creats a temporary local environment the objects works in ti and doesn't go out, along whit all the object in it!
#define the function
test1 <- function(){
  test_string <- 'This object is destroyed as soon as the function ends!'
  cat(test_string) #cat is similar to print; "a sorte of concatenete and print"
}
test1()


## global variable i
i <- 1
## define function
test2 <- function(){
  ## local variable i
  ## there is no i in the local environment -> search in parent environment
  i <- i * 10
  ## return
  return(i)
}
rm(i)

test2()
i <-i
test()



  




























































































































































