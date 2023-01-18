# Modules
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('/Users/max/Documents/python-challenge/PyBank/Resources/budget_data.csv')

# Open the CSV
with open(budget_csv, newline="", encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=",")
    
    csv_header = next(csv_reader) # Skip the first row
    # print(csv_header)
    
    # Empty list to hold csv data
    month_count = []
    profit = []
    change_profit = []
    
    # Iterate through the values to add to empty list
    for row in csv_reader:
        month_count.append(row[0])
        profit.append(int(row[1]))
          
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
        
# Utilize max() and min() function        
increase = max(change_profit)
decrease = min(change_profit)

# Utlize index function
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# Print results
print("  Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")     

# Write results to a .txt file 
output = os.path.join("analysis", 'output.txt')
with open(output,"w") as new:
    new.write("  Financial Analysis")
    new.write("\n")
    new.write("----------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")