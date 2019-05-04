# Import modules
import csv
import os

# Set path
py_bank_data = os.path.join("../PyBank", "budget_data.csv")

# Lists for storing data
profit = []
monthly_changes = []
date = []

# Create variables
month_count = 0
total_profit = 0
total_change_profit = 0
intital_profit = 0

# Open CSV
with open(py_bank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Append lists while going through the data
        month_count = month_count + 1
        date.append(row[0])
        profit.append(row[1])
        
        # Adding new profit to previous total profit
        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])
        
        # Find the change in profit per month
        monthly_changes_profits = final_profit - intital_profit
        monthly_changes.append(monthly_changes_profits)
        
        # Change final profit to inital profit for next row calculation
        initial_profit = final_profit

        # Adding all changing profits for average
        total_change_profit = total_change_profit + monthly_changes_profits
        

        # Average change over the given period
        average_change_profits = (total_change_profit/month_count)

        # Find the largest increase and decrease in profit per month      
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
        
        # Print output in GitBash
        print("Financial Analysis")
        print("----------------------------------------------------------")
        print("Total Months: " + str(month_count))
        print("Total Profits: " + "$" + str(total_profit))
        print("Average Change: " + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        print("----------------------------------------------------------")
    
    # Send to txt file 
    with open("bank_data_output.txt", "w") as text:
        text.write("Financial Analysis" + "\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Months: " + str(month_count) + "\n")
        text.write("Total Profits: " + "$" + str(total_profit) + "\n")
        text.write("Average Change: " + "$" + str(int(average_change_profits)) + "\n")
        text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")" + "\n")
        text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")" + "\n")
        text.write("----------------------------------------------------------\n")