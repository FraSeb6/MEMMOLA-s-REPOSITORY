
U_ <- runif(n = nsim)
u2 <- runif(n = nsim)

# Applica la trasformazione di Box-Muller
Z_0 <- sqrt(-2 * log(u1)) * cos(2 * pi * u2)
z2 <- sqrt(-2 * log(u1)) * sin(2 * pi * u2)

# Combina i risultati per ottenere n numeri casuali normali
c(z1, z2)

return(list(
  U_1=U_1,
  U_2,
  theta=theta,
  Z_0
))

set.seed(321)

nsim <- 1000
x11()

res_box_muller <- rnorm_01_box_muller(nsim = NSIM)

hhist(res_box_muller$Z_1)
mean(res_box_muller$Z_1)
var(res_box_muller$Z_1)

x_coord <- runif(nsim,-1,1)
y_coord <- runif(nsim,-1,1)

df_grains <- cbind(x_coord,y_coord)

plot(c(0,0),xlim=c(-1.2,1.2),ylim=c(-1.2,1.2),type="n", asp=1)
