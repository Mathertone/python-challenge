# Dependencies
import os
import csv

# Files
budget_csv = os.path.join("Resources", "budget_data.csv")

# Variables
date = []
revenue = []
revenue_change = []
difference_list = []
total_months = 1
total_profit_loss = 0
previous_revenue = 0
new_revenue = 0
counter = 0
dates_list = []

# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)

    row_1 = next(csvreader)

    previous = int(row_1[1])

    # Read through each row of data after the header
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        # get the difference
        diffrence = int(row[1]) - previous
        # now, save the current as previous so it's ready for the next iteration of the for loop
        previous = int(row[1])
        # add the difference that was just calculated to the difference list 
        difference_list.append(diffrence)
        # add the date to the dates list 
        dates_list.append(row[0])

    # ave change
    ave_change = round(sum(difference_list)/len(difference_list),2)
    # find the max increase 
    max_increase = max(difference_list)
    # find the index at which the max increase is sitting 
    index_max = difference_list.index(max_increase)
    # we get the greatest increase date by passing the greatest increase (money) id to the dates_list
    greatest_increase_date = dates_list[index_max]
    # find the min increase
    min_increase = min(difference_list)
    # find the index at which the min increase is sitting 
    index_min = difference_list.index(min_increase)
    # we get the greatest increase date by passing the greatest decrease (money) id to the dates_list
    greatest_decrease_date = dates_list[index_min]

# Print the outcomes
output = ( 
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: $ {ave_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${max_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${min_increase})\n"
)

print(output)
