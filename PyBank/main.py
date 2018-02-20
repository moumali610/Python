# Dataset 1

import os
import csv

pybank_csv = os.path.join("budget_data_1.csv")

# Lists to store data
Date = []
Revenue = []

with open(pybank_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
        
        
        
        