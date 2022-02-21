from textwrap import indent
from googlesearch import search
import csv

def browose(name):
    query = name + "Owner LinkedIn"

    for j in search(query, tld="co.in",num=1,stop=1,pause=2,verify_ssl=False):
        return j
            
with open('Sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    feildnames = ['No','Name','Main phone','City','Main email','Website Url','Address','Owner Name' ,'Owner Linkedin' ,'Owner Email' ]
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file,feildnames, delimiter = ',') 
        csv_writer.writeheader()
        for lines in csv_reader:
            name = lines["Name"]
            linkedIn = browose(name)
            lines["Owner Linkedin"] = linkedIn
            
            csv_writer.writerow(lines)