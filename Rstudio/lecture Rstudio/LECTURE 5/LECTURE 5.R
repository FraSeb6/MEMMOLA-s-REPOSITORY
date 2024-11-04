
x1 <- 1:10
y1 <- 10:1
plot(x1, y1) #THIS FUNCTION IS AN INVERSAL PROPORTIONAL FUNCTION
##  Customize the scatter plot
plot(x1, 
     y1, 
     col = "red", #you can do the same with the color code
     cex = 2, # dimension in default is 1
     pch = 20, # if you want you can write "A" and view letter, maybe something else
     xlab = "Hi!", 
     ylab = "", 
     main = "My second plot!") 

##  Add points to the existing plot
x2 <- runif(100, min = 0, max = 10) #randomly generate a point 
y2 <- runif(100, min = 0, max = 10)
plot(x1, y1, col = "red", cex = 2, pch = 20)
points(x2, y2, col = "blue", cex = 2, pch = 20)#useful for add a layer of point

##  Create a multi-plot layout
x11()   #it open a graphic windos 
par(mfrow = c(1, 2)) ##  1 row and 2 columns filled by row, this is useful for divide the canvas in 2 section, 
plot(x1, y1, type = "b", col = "red", cex = 2, pch = 20)
plot(x2, y2, col = "blue", cex = 2, pch = 20)

##  Close the plot device and reset parameters
dev.off()

par(mfrow = c(1, 1))



##  Adding segments to a plot
plot(x2, y2, xlim = c(-0.25, 10.25), ylim = c(-0.25, 10.25), pch = 20)
segments(
  x0 = c(0,   0, 10, 10, 0,   0), y0 = c(0,  10, 10,  0, 0,  10),  #it generate a segment for delimit the area where is the valaue
  x1 = c(0,  10, 10,  0, 10, 10), y1 = c(10, 10,  0,  0, 10,  0),
  lwd = 2, col = 2,  lty = 2
)

plot(x1, y1, col = 1:10, pch = 1:10, cex = 1:10 / 2, lwd = 3, xlab = "", ylab = "", xlim = c(0, 11), ylim = c(0, 11))


##create lines
x3 <- seq(from=-5,to= 5, by = 0.1)
plot(x3, sin(x3), type = "l", # l is line and b is point and lines; h area under the graph 
     ylab = "", xlab = "x", lwd = 2, col = "red")
lines(x3, cos(x3), lwd = 2, col = "blue")

##  Simple histogram
set.seed(1)  #when you set a seed you have set it, after you rerun it you you have different results  
x <- rnorm(n = 500)
hist(x)

##  Adjusting the number of breaks
hist(x, breaks = 30)

##  Overlaying density on a histogram
hist(x, breaks = 30, freq = FALSE)
lines(density(x), lwd = 2, col = grey(0.2), lty = 2) 

##  Plot a cubic function using curve()
curve(expr = x ^ 3 - x ^ 2 - 3 * x, from = -2, to = 2.5)
