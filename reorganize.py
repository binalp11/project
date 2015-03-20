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
    fixed = re.sub(r'"(\d+)","(.*?)","(.*?)","\s+([\d\.\,]+)","\s+([\d\.,]+)","\s+([\d\.\,]+)"', r'\1**\2**\3**\4**\5**\6', str(data_set))
    #send output to new file
    clean_data.write(fixed + '\n')  
    #close opened file
    clean_data.close()


#run function
fix_my_data()

#new function to fix the first line
def fix_1st_line():
    #open organized_data.txt 
    data_set = open("organized_data.txt")
    #read the file
    unfix = data_set.read()
    #use regex to fix the spacing of the header line
    fix_1st = re.sub(r'"(\w+)","(\w+)","(\w+)","(\w+\s\w+)","(\w+)","(\$)"',r'\1**\2**\3**\4**\5**\6', str(unfix))
    #reopen the file
    clean_data  = open('organized_data.txt', 'w')
    #write the new line to the file
    clean_data.write(fix_1st + '\n')

#run the function
fix_1st_line()



import pexpect

#spawn a shell prompt
child = pexpect.spawn('/bin/bash')
#remove everything after line 16699 to avoid error in split_by_line.py
child.sendline("head -n+16699 organized_data.txt > organized_data2.txt")

