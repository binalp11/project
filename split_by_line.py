#! /bin/bash
        
import re

clean_data = open("cleaned_species_methods.txt", 'w')
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
        fields[2] = re.sub(r'(Bag Nets|Cast Nets|Dip Nets|Encircling Nets \(Purse\)|Entangling Nets \(Gill\) Unspc|Fyke and Hoop Nets|Trammel Nets|Lampara \& Ring Nets|Purse Seines|Haul Seines)', r'Nets', fields[2]) 
        fields[2] = re.sub(r'(Beam Trawls|Trawls|Otter Trawl Bottom|Otter Trawl Midwater|Netstrawl)', r'Trawls', fields[2]) 
        fields[2] = re.sub(r'(Dredge Clam|Dredge Other|Dredge Oyster|Dredge Scallop)', r'Dredge', fields[2])
        fields[2] = re.sub(r'(Gill Nets|Gill Nets, Barracuda|Gill Nets, Other|Gill Nets, Salmon|Gill Nets, Sea Bass|Gill NetsHalibut)', r'Gill Nets', fields[2])
        fields[2] = re.sub(r'(Pots|Pots And Traps|Pots And Traps\(frhwa\)|Pots And Traps, Dungens|Pots And Traps, King|Pots And Traps, Other|Pots And TrapsLobster)', r'Pots and Traps', fields[2])
        fields[2] = re.sub(r'(Lines Hand|Lines Jigging Machine|Lines Long Set With Hooks|Lines Power Troll Other|Lines Troll|Troll \& Hand Lines Cmb)', r'Lines', fields[2])
        fields[3] = re.sub(r',', r'', fields[3])
        fields[4] = re.sub(r',', r'', fields[4])
        fields[5] = re.sub(r',', r'', fields[5])
        newline = '\t'.join(fields)
        clean_data.write(newline)



