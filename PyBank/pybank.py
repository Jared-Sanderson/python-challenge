import os
import csv

# bank_csv = os.path.join("Resources","budget_data.csv")
bank_csv = os.path.join("/Users/Jared/Desktop/DATA HW/python-challenge/PyBank/Resources/budget_data.csv")

# List to store data
netprofit = []
monthly = []
date = []

# The variables needed
#The total number of months included in the dataset
months = 0
#The net total amount of "Profit/Losses" over the entire period
totalprofit = 0 
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
total_change = 0

start_profit = 0
avg_change = 0
last_month = 867884
largest_increase = 0
largest_loss = 0
# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:

with open(bank_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        months= months +1
        totalprofit = totalprofit + int(row[1])
        current_change = (int(row[1]) - last_month)
        total_change = total_change + current_change
        if current_change > largest_increase:
            largest_increase = current_change
            max_day = row[0]
            max_profits = current_change
        if current_change < largest_loss:
            largest_loss = current_change
            min_day = row [0]
            min_profits = current_change
        last_month = int(row[1])
        last_month_change = current_change
avg_change = format((total_change/(months - 1)),".2f")

#Print to look similar to example

print("The Financial Analsis") 
print("----------------------------")
print("The Total Months: " + str(months))
print("The Total: " + "$" + str(totalprofit))        
print("Average Change: " + "$" + str(avg_change))
print("Greates Increase in Profits: " + str(max_day) + "($" + str(max_profits)+")")
print("Greates Decrease in Profits: " + str(min_day) + "($" + str(min_profits)+")")


with open('/Financial_Analysis.txt', "w") as text:
    text.write("The Financial Analsis") 
    text.write("----------------------------")
    text.write("The Total Months: " + str(months))
    text.write("The Total: " + "$" + str(totalprofit))        
    text.write("Average Change: " + "$" + str(avg_change))
    text.write("Greates Increase in Profits: " + str(max_day) + "($" + str(max_profits)+")")
    text.write("Greates Decrease in Profits: " + str(min_day) + "($" + str(min_profits)+")")