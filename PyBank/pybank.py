import os
import csv

bank_csv = os.path.join("Resoucres","budget_data.csv")

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
profit_change = 0

start_profit = 0

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:

with open(bank_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
 
    for row in csvreader:

            months = months + 1

            date.append(row[0])

            netprofit.append(row[1])

            totalprofit = totalprofit + int(row[1])
#Need start and final profit to find the changes per month
finalprofit = int(row[1])
monthlychanges = finalprofit - start_profit

#store the monthly changes to the monthly list
monthly.append(monthlychanges)
#add to the change variable
profit_change = profit_change + monthlychanges
#reset start profit
start_profit = finalprofit

#Find average now
avg_change = (profit_change/months)

#Find MAX and MIN
max_profits = max(monthly)
min_profits = min(monthly)

max_day = date[monthly.index(max_profits)]
min_day = date[monthly.index(min_profits)]

#Print to look similar to example

print("The Financial Analsis") 
print("----------------------------")
print("The Total Months: " + str(months))
print("The Total: " + "$" + str(totalprofit))        
print("Average Change: " + "$" + str(int(avg_change)))
print("Greates Increase in Profits: " + str(max_day) + "($" + str(max_profits)+")")
print("Greates Decrease in Profits: " + str(max_day) + "($" + str(min_profits)+")")