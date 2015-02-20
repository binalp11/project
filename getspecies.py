#! /bin/bash


#this code is to get the list of species from the NOAA commercial landings website

#import packages
from bs4 import BeautifulSoup
import re


def getspecies():

    #get soup from the saved page
    soup = BeautifulSoup(open('species.html'))
    #find form section of soup
    form_pane = soup.find("form")
    #find all the option sections which hold the species
    species_names = form_pane.find_all("option")
    #use regex to get just the name of the species
    all_names = re.sub(r'<option>(.*?)</option>,', r'\1\n', str(species_names))
    #open a new text file to save the output to
    names  = open('names_list.txt', 'w')
    #write output to file
    names.write(all_names)
    #close the file
    names.close()
    print "The species list has been created"

getspecies()
