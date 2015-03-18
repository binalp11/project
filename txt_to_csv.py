import csv
import re 

def convertocsv(txtname, csvname):
    txt_file = "{}".format(txtname)
    csv_file = r"{}".format(csvname)
    in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
    out_csv = csv.writer(open(csv_file, 'w'))
    out_csv.writerows(in_txt)


convertocsv("cleaned_species_methods.txt", "final_data.csv")