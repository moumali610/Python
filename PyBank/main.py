import os
import csv
 
pyBank_csv = os.path.join("budget_data_1.csv")
 
 
# Lists to store data
date = []
revenue = []
rev_change = []
 
with open(pyBank_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
  


# Loops from the second row
    next(csvreader, None)

    for row in csvreader:
       date.append(row[0])
       revenue.append(int(row[1]))
       # print(row)
       

# Financial Analysis Report
print("                            ")
print("Financial Analysis")
print("----------------------------")

# Finding Total Months by finding lenth of dataset
print("Total Months: $" + (str(len(date)))) 

#Finding Total Revenue by find the sum of the Revenue List
#print("Total Revenue: ")


# TotalRevenue = 0
def sum(revenue):
    total = 0
    for x in revenue:
        total = total + x
    return total

TotalRevenue = sum(revenue)
print("Total Revenue: " + str(TotalRevenue))


# The average change in revenue between months over the entire period 

for i in range(len(revenue) - 1):
    rev_change.append(int(revenue[i + 1]) - int(revenue[i]))
    avg_rev_change = sum(rev_change)/len(rev_change)
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)

    max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
   
    
#print(avg_rev_change)

print("Average Revenue Change: $" + str(avg_rev_change))
print("Greatest Increase in Revenue: " + max_rev_change_date + "($", max_rev_change,")")
print("Greatest Decrease in Revenue: " + min_rev_change_date + "($", min_rev_change,")")
# The greatest increase in revenue (date and amount) over the entire period


# The greatest decrease in revenue (date and amount) over the entire period




#avg_rev_change = 0
#def sum(rev_change):
#    avg_rev_change = sum(rev_change)/len(rev_change)
#    for i in range(1, len(revenue)):
#        revenue.append(revenue[i] - revenue [i-1])
#    return avg_rev_change
#print(avg_rev_change)
#AverageChange = sum(rev_change)
#print(AverageChange)

# average = sum(numlist) / len(numlist)



import os
import csv
 
pyBank_csv = os.path.join("budget_data_2.csv")
 
 
# Lists to store data
date = []
revenue = []
rev_change = []
 
with open(pyBank_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
  


# Loops from the second row
    next(csvreader, None)

    for row in csvreader:
       date.append(row[0])
       revenue.append(int(row[1]))
       # print(row)
       

# Financial Analysis Report
print("                            ")
print("Financial Analysis")
print("----------------------------")

# Finding Total Months by finding lenth of dataset
print("Total Months: " + (str(len(date)))) 

#Finding Total Revenue by find the sum of the Revenue List
#print("Total Revenue: ")


# TotalRevenue = 0
def sum(revenue):
    total = 0
    for x in revenue:
        total = total + x
    return total

TotalRevenue = sum(revenue)
print("Total Revenue: $" + str(TotalRevenue))


# The average change in revenue between months over the entire period 

for i in range(len(revenue) - 1):
    rev_change.append(int(revenue[i + 1]) - int(revenue[i]))
    avg_rev_change = sum(rev_change)/len(rev_change)
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)


    max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
  

print("Average Revenue Change: $" + str(avg_rev_change))
print("Greatest Increase in Revenue: " + max_rev_change_date + "($", max_rev_change,")")
print("Greatest Decrease in Revenue: " + min_rev_change_date + "($", min_rev_change,")")


