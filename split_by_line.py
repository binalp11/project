#! /bin/bash
        
import re

new_data = open("new_data.txt", 'w')
with open("organized_data.txt") as data:
    for line in data:
        fields = line.split('\t')
        fields[1] = re.sub(r'(\w+),\s(\w+)(\s{0,1})(\w+){0,1}', r'\1',fields[1])
        fields[2] = re.sub(r'(\w+),\s(\w+)(\s{0,1})', r'\1', fields[2])
        fields[3] = re.sub(r',', r'', fields[3])
        fields[4] = re.sub(r',', r'', fields[4])
        fields[5] = re.sub(r',', r'', fields[5])
        newline = '\t'.join(fields)
        new_data.write(newline)



