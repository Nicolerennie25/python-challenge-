import csv

# Define file path
file_path = "C:\\Users\\n.rennie\\Documents\\Python-challenge\\python-challenge-\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Iterate through rows
    for row in csvreader:
        # Update total number of months
        total_months += 1
        
        # Update net total amount of profit/losses
        net_total += int(row[1])

        # Calculate change in profit/losses and append to changes list
        if total_months > 1:
            change = int(row[1]) - prev_profit
            changes.append(change)
        
        # Update previous profit/loss for next iteration
        prev_profit = int(row[1])

        # Check for greatest increase and decrease in profits
        if total_months > 1:
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

# Calculate average change
average_change = sum(changes) / len(changes)

# Print analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export results to text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"Results have been saved to '{output_file}'.")

