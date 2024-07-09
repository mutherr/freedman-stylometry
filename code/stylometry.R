library(stylo)
library(rstudioapi)

# Getting the path of your current open file
current_path = rstudioapi::getActiveDocumentContext()$path 
setwd(dirname(current_path ))

x = stylo()

summary(x)
x$features.actually.used
