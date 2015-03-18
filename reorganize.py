#! /bin/bash

#import packages    
import re


#open new file to send output to called organized_data.txt
clean_data  = open('organized_data.txt', 'w')

#define a funciton to use regex and fix data into columns seperated by tabs
def fix_my_data():
    clean_data  = open('organized_data.txt', 'w')
    #open data set
    data_set = open("data_w_o_header.txt").read()
    #use regex to fix spacing between columns
    fixed = re.sub(r'"(\d+)","(.*?)","(.*?)","\s+([\d\.\,]+)","\s+([\d\.,]+)","\s+([\d\.\,]+)"', r'\1\t\2\t\3\t\4\t\5\t\6', str(data_set))
    #send output to new file
    clean_data.write(fixed + '\n')  
    clean_data.close()


#run function
fix_my_data()

def fix_1st_line():
    data_set = open("organized_data.txt")
    unfix = data_set.read()
    fix_1st = re.sub(r'"(\w+)","(\w+)","(\w+)","(\w+\s\w+)","(\w+)","(\$)"',r'\1\t\2\t\3\t\4\t\5\t\6', str(unfix))
    clean_data  = open('organized_data.txt', 'w')
    clean_data.write(fix_1st + '\n')

fix_1st_line()