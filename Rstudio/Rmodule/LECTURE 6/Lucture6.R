head(iris,3)
iris_tbl <- tibble::as_tibble(iris)
iris_tbl
head(iris$Spe,3)
iris_tbl$Spe
head(iris[,1])
iris_tbl[,1]
library(ggplot2)
data(mpg)
# tibble::glimpse(mpg)



ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy))

ggplot(data = DATA) +
  GEOM_FUNCTION(mapping = aes(MAPPINGS))

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class))



ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, size = drv))

ggplot(data = mpg) + geom_point(mapping = aes(x = displ, y = hwy),shape="x", col = "blue") 




ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy))
#in the last part we have more variance, because we have more sport car

x11()
ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, linetype = drv))

x11()
ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, col=class)) +
  geom_point(mapping = aes(x = displ, y = hwy, col=class))

ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(col = class)) +
  geom_smooth()


x11()
ggplot(data = mpg, mapping = aes(x = displ, y = hwy, col = class)) +
  geom_point(size = 3, alpha = 0.7) +  # Larger points with transparency
  geom_smooth(se = FALSE, linetype = "dashed", linewidth = 1.2,span=1.5) +  # Smoother lines without confidence interval
  scale_color_brewer(palette = "Set1") +  # Use a colorblind-friendly palette
  labs(
    title = "Fuel Efficiency vs Engine Displacement",
    subtitle = "Relationship between engine size and highway fuel efficiency across car types",
    x = "Engine Displacement (liters)",
    y = "Highway Fuel Efficiency (mpg)",
    color = "Vehicle Class"
  ) + 
  theme_minimal(base_size = 15) +  # Clean minimalistic theme
  theme(
    plot.title = element_text(face = "bold", size = 18, hjust = 0.5),
    plot.subtitle = element_text(size = 14, hjust = 0.5),
    legend.position = "bottom",  # Move legend to the bottom
    legend.title = element_text(size = 12),
    legend.text = element_text(size = 10),
    legend.background = element_rect(fill = "gray95", color = NA)
  )
#########################################
gg_bar <- ggplot(mpg) +
  geom_bar(aes(x=drv)) +
  theme_bw()

gg_bubble <- ggplot(data = mpg) +
  geom_point(mapping = aes(
    x = displ,
    y = hwy,
    size = cyl,
    color = cyl,
    alpha = cyl
  )) +
  scale_color_viridis_c(option = "C") +
  theme_bw()
#####
library(patchwork)
gg_bar +
  gg_bubble


library(patchwork)
gg_bar /
  gg_bubble


library(patchwork)
(gg_bar + gg_bar)/
  gg_bubble




################################################################################
####excise###



