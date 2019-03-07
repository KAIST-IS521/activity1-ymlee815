import csv
import re

with open('data.csv', 'r', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar ='"', quoting = csv.QUOTE_ALL)
    
    for line in reader:
        line = [wd.replace('\r\n', '') for wd in line]
        print(line)

