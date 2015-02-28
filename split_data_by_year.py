#! /bin/bash

#makes a function that takes an input, year. Goes through large data set, and if a line is found from that 
#year then it will output it to the file of the corresponding year
def year_lines(the_year):
    #import large dataset
    print "Working on year:" + str(the_year)
    data = open('/home/vagrant//project/organized_data.txt').readlines()
    #make a file for the year in question
    yearfile = open('{}.txt'.format(the_year), 'w')
    #for loop for each line in data
    for line in data:
        #if the line starts with that year then add it to the new corresponding file
        if line.startswith("{}".format(the_year)):
            yearfile.write(line)
        

#for each year in the range run the funciton
for year in range(1950,2014):
    year_lines(year)

