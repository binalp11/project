
data = read.csv("final_data.csv")
species = c("BARRACUDA","ECHINODERMS","FLOUNDER","HAKE","MACKERAL","SEA BASS", "TUNA", "SALMON", "YELLOWTAIL JACK", "SARDINE", "SHARK")

speciesdata <- data %>% group_by(Year, Species) %>% summarise(sum(Pounds))

plotspecies <- function(name){
  library(dplyr)
  two <- speciesdata %>% filter(Species == name)
  file_name <- paste(name,".png")
  elyear1 = c(1957,1958, 1958,1957)
  elyear2 = c(1965,1966,1965,1966)
  elyear3 = c(1972,1973,1973,1972)
  elyear4 = c(1982,1983,1983,1982)
  elyear5 = c(1987,1988,1988,1987)
  elyear6 = c(1997,1998,1998,1997)
  y = c(0,0,10000000000000000000000,100000000000000000000)
  png(file_name)
  plot(two$Year, two$"sum(Pounds)", type = 'l', main = name, xlab = 'Year', ylab = "Pounds")
  polygon(elyear1,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear2,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear3,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear4,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear5,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear6,y,col= rgb(1,0,0, .1), border=NA)
  dev.off()
}


plotspecies("SOLE")

geardata <- data %>% group_by(Year, Gear) %>% summarise(sum(Pounds))

plotgear <- function(name){
  library(dplyr)
  two <- geardata %>% filter(Gear == name)
  file_name <- paste(name,".png")
  elyear1 = c(1957,1958, 1958,1957)
  elyear2 = c(1965,1966,1965,1966)
  elyear3 = c(1972,1973,1973,1972)
  elyear4 = c(1982,1983,1983,1982)
  elyear5 = c(1987,1988,1988,1987)
  elyear6 = c(1997,1998,1998,1997)
  y = c(0,0,10000000000000000000000,100000000000000000000)
  png(file_name)
  plot(two$Year, two$"sum(Pounds)", type = 'l', main = name, xlab = 'Year', ylab = "Pounds")
  polygon(elyear1,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear2,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear3,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear4,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear5,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear6,y,col= rgb(1,0,0, .1), border=NA)
  dev.off()
}


plotgear("Lines")
