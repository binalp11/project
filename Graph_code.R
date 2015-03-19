#import packages 
library(dplyr)

#reads the csv file 
data = read.csv("final_data.csv")

#uses dplyer to group the year and species together and sum the pounds caught for each species for each year
speciesdata <- data %>% group_by(Year, Species) %>% summarise(sum(Pounds))

#this fucntion makes a plot for the entered species name
plotspecies <- function(name){
  #imports dplyr into the function
  library(dplyr)
  #uses dplyr to filter out only the speices to be graphed
  two <- speciesdata %>% filter(Species == name)
  #creates a file name with the species name
  file_name <- paste(name,".png")
  #elyear 1-6 are the years of el nino, entered in format to make a polygon
  elyear1 = c(1957,1958, 1958,1957)
  elyear2 = c(1965,1966,1965,1966)
  elyear3 = c(1972,1973,1973,1972)
  elyear4 = c(1982,1983,1983,1982)
  elyear5 = c(1987,1988,1988,1987)
  elyear6 = c(1997,1998,1998,1997)
  #y is how tall the polygon will be
  y = c(0,0,10000000000000000000000,100000000000000000000)
  #opens a new image file for the graph to be saved to, named after file_name
  png(file_name)
  #plots the pounds on the y axis and the years on the x axis
  plot(two$Year, two$"sum(Pounds)", type = 'l', main = name, xlab = 'Year', ylab = "Pounds")
  #next 6 lines makes red transparent polygons for the el nino years
  polygon(elyear1,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear2,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear3,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear4,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear5,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear6,y,col= rgb(1,0,0, .1), border=NA)
  #closes the image file
  dev.off()
}

#uses dplyer to group the data by year and gear, then added the total pounds for over the years
geardata <- data %>% group_by(Year, Gear) %>% summarise(sum(Pounds))

#this function makes a plot for the entered gear to be graphed
plotgear <- function(name){
  #import dplyr into the function
  library(dplyr)
  #uses dplyer to filter out only the gear to be graphed
  two <- geardata %>% filter(Gear == name)
  #opens a new image file for the graph to be saved to, named after file_name
  file_name <- paste(name,".png")
  #elyear 1-6 are the years of el nino, entered in format to make a polygon
  elyear1 = c(1957,1958, 1958,1957)
  elyear2 = c(1965,1966,1965,1966)
  elyear3 = c(1972,1973,1973,1972)
  elyear4 = c(1982,1983,1983,1982)
  elyear5 = c(1987,1988,1988,1987)
  elyear6 = c(1997,1998,1998,1997)
  #y is how tall the polygon will be
  y = c(0,0,10000000000000000000000,100000000000000000000)
  #opens a new image file for the graph to be saved to, named after file_name
  png(file_name)
  #plots the pounds on the y axis and the years on the x axis
  plot(two$Year, two$"sum(Pounds)", type = 'l', main = name, xlab = 'Year', ylab = "Pounds")
  #next 6 lines makes red transparent polygons for the el nino years
  polygon(elyear1,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear2,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear3,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear4,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear5,y,col= rgb(1,0,0, .1), border=NA)
  polygon(elyear6,y,col= rgb(1,0,0, .1), border=NA)
  #closes the image file
  dev.off()
}


#here are some examples

plotspecies("TUNA")
plotspecies("SOLE")
plotspecies("SARDINE")


plotgear("Lines")
plotgear("Nets")

 