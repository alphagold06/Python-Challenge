import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    rowcounter = 0
    total_budget = 0
    dateVal = []
    profit_loss = []
    rev_change = []


# Loop through the data row by row
    for row in csvreader:
        # Get the total from index data element 1 and store in variable total
        total = int(row[1])

        # Sum the total and add to total_budget
        total_budget += total

        #Add 1 to rowcounter to move to next row
        rowcounter += 1

        # Get total value and append to profit_loss list
        profit_loss.append(total)
        
        # Get date and append to dateVal list
        dateVal.append(row[0])

    for i in range (0, rowcounter - 1):
        rev_change.append(int(profit_loss[i+1]) - int(profit_loss[i]))

average_change = round(sum(rev_change)/len(rev_change),2)

maximum = max(rev_change)

max_index = rev_change.index(maximum) + 1

date_max = dateVal[max_index]

minimum = min(rev_change)

min_index = rev_change.index(minimum) + 1

date_min = dateVal[min_index]

print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(rowcounter))
print("Total:" + "$" + str(total_budget))
print("Average Change:" + str(average_change))
print("Greatest Increase in Profits: " + str(date_max) + " (" + str(maximum) + ")" )
print("Greatest Decrease in Profits: " + str(date_min) + " (" + str (minimum) + ")" )

# Specify the file to write to
output_path = os.path.join("..", "Resources", "budgetdata.txt")

# Open the file using "write" mode. Specify the variable f to hold the contents
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-----------------------------------\n")
    f.write("Total Months: " + str(rowcounter) + "\n")
    f.write("Total:" + "$" + str(total_budget) + "\n")
    f.write("Average Change:" + str(average_change) + "\n")
    f.write("Greatest Increase in Profits: " + str(date_max) + " (" + str(maximum) + ")" + "\n")
    f.write("Greatest Decrease in Profits: " + str(date_min) + " (" + str (minimum) + ")" )