
# 1 The total number of months included in the dataset
# 2 The net total amount of "Profit/Losses" over the entire period
# 3 The average of the changes in "Profit/Losses" over the entire period
# 4 The greatest increase in profits (date and amount) over the entire period
# 5 The greatest decrease in losses (date and amount) over the entire period
# 6 Print the analysis to the terminal and export a text file with the results


# import functions
import os
import csv

# set parameters
months = []
P_L_delta = []

month_counter = 0
P_L_net = 0
P_L_last_month = 0
P_L_this_month = 0
P_L_M_change = 0

# write path
budget_csv_path = os.path.join("Resources", "budget_data.csv")

# read csv file
with open(budget_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # csv has a header - read it first
    csv_header = next(csvfile)

    # print header values
    print(f"Header: {csv_header}")
        
    # loop through data after the header
    for row in csv_reader:

        # count months
        month_counter += 1

        # determine net total amount of P&L
        P_L_this_month = int(row[1])
        P_L_net += P_L_this_month

        if (month_counter == 1):
            # if there is no change in month
            P_L_last_month = P_L_this_month
            continue

        else:

            # else compute the difference
            P_L_M_change = P_L_this_month - P_L_last_month

            # append month to the months value
            months.append(row[0])

            # append P_L_M_change to the P_L_delta value
            P_L_delta.append(P_L_M_change)

            # connect current_month_loss to be P_L_last_month as loop restarts
            P_L_last_month = P_L_this_month

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(P_L_delta)
    average_profit_loss = round(sum_profit_loss/(month_counter - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(P_L_delta)
    lowest_change = min(P_L_delta)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = P_L_delta.index(highest_change)
    lowest_month_index = P_L_delta.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# print a readout to git bash
print("Financial Analysis")
print("-----------------------------------------------")
print(f"Total Months:  {month_counter}")
print(f"Total:  ${P_L_net}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# write to a text file
budget_file = os.path.join("Resources", "budget_data.txt")
with open(budget_file, "w") as output:

    output.write("Financial Analysis\n")
    output.write("--------------------------------------------\n")
    output.write(f"Total Months:  {month_counter}\n")
    output.write(f"Total:  ${P_L_net}\n")
    output.write(f"Average Change:  ${average_profit_loss}\n")
    output.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    output.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")