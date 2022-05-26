#Dependencies
import os
import csv

# Specify the path for file

csvpath = os.path.join("Resources","budget_data.csv")

# Create the lists 

profit = []
monthly_changes = []
date = []

# Define variables
 
count = 0
total_profit = 0
total_profit_change = 0
initial_profit = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:    
      # counting number of months in the dataset 
      count = count + 1 

      #append data and the profit information
      date.append(row[0])
      profit.append(row[1])

      #calculate the total profit
      total_profit = total_profit + int(row[1])

      #Average change in profits from month to month
      final_profit = int(row[1])

      #Average change in profits
      monthly_profit_change = final_profit - initial_profit

      #Append monthly changes in a list
      monthly_changes.append(monthly_profit_change)

      total_profit_change = total_profit_change + monthly_profit_change
      initial_profit = final_profit

      #Calculate the average change in profits
      average_profit_change = (total_profit_change/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

      
    #print result to Terminal
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_profit_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

#print output to text file
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_profit_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")