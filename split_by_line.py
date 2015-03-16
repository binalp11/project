#! /bin/bash
        
import re

new_data = open("new_data.txt", 'w')
with open("organized_data.txt") as data:
    for line in data:
        fields = line.split('\t')
        fields[1] = re.sub(r'(\w+),\s(\w+)(\s{0,1})(\w+){0,1}', r'\1',fields[1])
        fields[1] = re.sub(r'(BARRACUDA|HERRING|EEL|FLOUNDER|ABALONE|TUNA|SOLE|CRAB|SMELT|SHARK|SEAWEED|SQUID|SKATE|GREENLING)([S]{1})', r'\1',fields[1])
        fields[1] = re.sub(r'(THRESHER SHARK)', r'SHARK', fields[1])
        fields[1] = re.sub(r'(ANCHOVIES)', r'ANCHOVY', fields[1])
        fields[1] = re.sub(r'(CARPS AND MINNOW)', r'CARP', fields[1])  
        fields[1] = re.sub(r'(CLAMS OR BIVALVES|CLAM|BIVALVES|OYSTER|CLAM, GAPER|MUSSEL)', r'BIVALVES', fields[1])
        fields[1] = re.sub(r'(FINFISHES AND ANIMAL FOOD|FINFISHES FOOD|FINFISHES, OTHER|FINFISHES, ORNAMENTAL)', r'FINFISHES', fields[1])  
        fields[1] = re.sub(r'(STARFISH|SEA URCHINS|SEA CUCUMBER)', r'ECHINODERM', fields[1]) 
        fields[1] = re.sub(r'(HAKE\(WHITING\))', r'HAKE', fields[1])
        fields[1] = re.sub(r'(HALIBUT|FLOUNDER)', r'FLATFISH', fields[1])
        fields[1] = re.sub(r'(JACK MACKEREL|MACKEREL \(SCOMBER\))', r'MACKEREL', fields[1]) 
        fields[1] = re.sub(r'(SEABASS)', r'SEA BASS', fields[1]) 
        fields[2] = re.sub(r'(\w+),\s(\w+)(\s{0,1})', r'\1', fields[2])
        fields[3] = re.sub(r',', r'', fields[3])
        fields[4] = re.sub(r',', r'', fields[4])
        fields[5] = re.sub(r',', r'', fields[5])
        newline = '\t'.join(fields)
        new_data.write(newline)



