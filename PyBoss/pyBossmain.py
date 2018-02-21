import os
import csv


EmployeeData1_csv = os.path("python-challenge","PyBoss","employee_data1.csv")
with open(EmployeeData1_csv, newline="") as csvfile:
   csvreader= csv.reader(csvfile, delimiter=",")

   for row in csv_reader:
       print(row)