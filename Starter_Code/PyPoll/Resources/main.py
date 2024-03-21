import csv

# Define the file path
file_path = "C:\\Users\\n.rennie\\Documents\\Python-challenge\\python-challenge-\\Starter_Code\\PyPoll\\Resources\\election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(csvreader)

    # Loop through each row in the CSV
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Get candidate name from the row
        candidate_name = row[2]

        # If candidate is not in the list of candidates, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate
        candidate_votes[candidate_name] += 1

# Initialize variables for winner calculation
winner = ""
max_votes = 0

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print each candidate's results
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if this candidate has more votes than the current winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a text file
with open("election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

print("Results have been saved to 'election_results.txt'.")
