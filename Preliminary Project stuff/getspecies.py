#! /bin/bash


#this code is to get the list of species from the NOAA commercial landings website

#import packages
from bs4 import BeautifulSoup
import re


def getspecies():
    #open a new text file to save the output to
    nameslist  = open('names_list.txt', 'w')
    #get soup from the saved page
    soup = BeautifulSoup(open('species.html'))
    #find form section of soup
    form_pane = soup.find("form")
    #find all the option sections which hold the species
    species_names = form_pane.find_all("option")
    #get species string from species name 
    for species in species_names:
        #save species from
        all_names =  species.string + '\n'
        #write output to file
        nameslist.write(all_names)
        


getspecies()
