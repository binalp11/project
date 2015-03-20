#import packages
import csv
import re 

#this function converts a tab delimited file into a csv file
def convertocsv(txtname, csvname):
    #takes the name of the original file
    txt_file = "{}".format(txtname)
    #takes the name of the new csv file
    csv_file = r"{}".format(csvname)
    #opens and reads the txt file
    in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
    #outputs it as a csv ffile
    out_csv = csv.writer(open(csv_file, 'w'))
    #writes the file to the output file
    out_csv.writerows(in_txt)

#runs the file for the files in my project
convertocsv("final_data.txt", "final_data.csv")