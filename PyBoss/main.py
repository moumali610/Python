import os
import csv
from US_abbrev import US_abbrev as USAb

pyBoss_csv = os.path.join("employee_data1.csv")

# Lists to store data
Emp_ID = []
Name = []
dob = []
SSN = []
State = []

with open(pyBoss_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    # Loops from the second row
    next(csvreader, None)
    
    for row in csvreader:
       Emp_ID.append(row[0])
       Name.append(row[1])
       dob.append(row[2])
       SSN.append(row[3])
       State.append(row[4])
       #print(row)

# Current List Format:
    # Emp ID,Name,DOB,SSN,State
    # 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
    
# Convert and export the data to use the following format instead:
   # Emp ID,First Name,Last Name,DOB,SSN,State
   # 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
