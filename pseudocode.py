#this is the preliminary pseudocode for my final project



#get data from NOAA/internet:

    #get list of species that have data on the NOAA commercial landings site
        #link is on this page: http://www.st.nmfs.noaa.gov/commercial-fisheries/commercial-landings/landings-by-gear/index

   # get landings data of each fishing method
        #use list of species to get data for each fishing method from 1950 to 2013 in California

    #get landings data of each species in California
        #use list of species to get data over the years 1950 to 2013

    #get Sea surface temperature or pressure data over the years 1950-2013 to Determine El Nino years


#organize data 
    
    #if for any species there are no landings in California, then remove it from list

    #sort fishing methods into broader categories
        #there are many methods that are species specific (example: Dredge Clam and Dredge Crab, should be combined into Dredge)

    #Group species into higher taxonomy to reduce number of species
        #not too sure how this can be done (maybe use encyclopedia of life??)


#calculations
    
    #calculate the percent weight of landings each method gets
    #calculate the monetary value of landings each method gets


#determine el nino years
    
    #somehow use SST or SSP pressure to find El Nino occurances

#graphs
    
    #use R to graph the percent weight and monetary value for each method over time
    #use R to graph the grouped taxonomy landings data over time 

    #for each graph mark El Nino years 

