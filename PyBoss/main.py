import os
import csv

# from US_abbrev.py saved in same directory as main.py, import us_state_abbrev = {} , set it as variable
from US_abbrev import us_state_abbrev as US_abbrev

# Paths to collect data from
employee_data_path1 = os.path.join('employee_data1.csv')
employee_data_path2 = os.path.join('employee_data2.csv')

# Create List to store data and ["Add Headers"]
ID = ["Employee ID"]
firstName = ["First Name"]
lastName = ["Late Name"]
DoB = ["DoB"]
SSN = ["SSN"]
State = ["State"]

# Opening Dataset 1 and using [indexes] and split() to select the specific objects you want
with open(employee_data_path1, newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")

	next(csvreader,None)
	for row in csvreader:
		ID.append(row[0])
		firstName.append(row[1].split()[0])
		lastName.append(row[1].split()[1])
		DoB.append(row[2].split("-")[1]+"/"+row[2].split("-")[2]+"/"+row[2].split("-")[0])
		SSN.append("***-**-"+row[3].split("-")[2])
		State.append(US_abbrev[row[4]])

# Opening Dataset 2 and using [indexes] and split() to select the specific objects you want
with open(employee_data_path2, newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")

	next(csvreader,None)
	for row in csvreader:
		ID.append(row[0])
		firstName.append(row[1].split()[0])
		lastName.append(row[1].split()[1])
		DoB.append(row[2].split("-")[1]+"/"+row[2].split("-")[2]+"/"+row[2].split("-")[0])
		SSN.append("***-**-"+row[3].split("-")[2])
		State.append(US_abbrev[row[4]])

csv_file_path_new = os.path.join('employee_data_new.csv')


# Open the output file
with open(csv_file_path_new,mode="w", newline="") as csvfile:
	csvwriter = csv.writer(csvfile,delimiter=",")
	# Zip Lists together
	for row in zip(ID,firstName,lastName,DoB,SSN,State):
		csvwriter.writerow(row)