# Modules
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('/Users/max/Documents/python-challenge/PyPoll/Resources/election_data.csv')

# Dictionary to store data
votes_per_candidate = {}

# Total rows
total_votes = 0

# Open the CSV
with open(election_csv, newline="", encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=",")
    
    csv_header = next(csv_reader) # Skip the first row
    # print(csv_header)
    
    # # Iterate through the values to add to dictionary
    for row in csv_reader:
        total_votes += 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1

# Print results                
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
 
for candidate, votes in votes_per_candidate.items():
     print(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")")
     
winner = max(votes_per_candidate, key=votes_per_candidate.get)
     
print("-------------------------") 
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a .txt file 
output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Election Results")
    new.write('\n')
    new.write("-------------------------")
    new.write('\n')
    new.write("Total Votes: " + str(total_votes))
    new.write('\n')
    new.write("-------------------------")
    new.write('\n')

    for candidate, votes in votes_per_candidate.items():
        new.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")")
        new.write('\n')
    
    new.write("-------------------------") 
    new.write('\n')
    new.write(f"Winner: {winner}")
    new.write('\n')
    new.write("-------------------------")