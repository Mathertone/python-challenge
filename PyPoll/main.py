# Dependencies
import os
import csv

# Files
election_csv = os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0
candidates = []
candidates_percentage = []
candidates_total_votes = []
max_votes = 0
max_index = 0

# Open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)  

    # Read through each row of data after the header
    for row in csvreader:
        # Total number of votes
        total_votes += 1
        
        # Candidate name
        candidate_name = row[2]

        # Candidate vote tally
        if candidate_name in candidates:
            candidate_index = candidates.index(candidate_name)
            candidates_total_votes[candidate_index] = candidates_total_votes[candidate_index] + 1
        else:
            candidates.append(candidate_name)
            candidates_total_votes.append(1)

        # Candidate Voter Percentage
    for x in range(len(candidates)):
        voter_percentage = round(candidates_total_votes[x]/total_votes*100,3)
        candidates_percentage.append(voter_percentage)
        
        if candidates_total_votes[x] > max_votes:
            max_votes = candidates_total_votes[x]
            max_index = [x]
   
    winner_index = max(candidates_total_votes)
    winner_votes_index = candidates_total_votes.index(winner_index)

    election_winner = candidates[winner_votes_index]

output = ( 
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------\n"
    f"{str(candidates[0])}: {str(candidates_percentage[0])}% ({str(candidates_total_votes[0])})\n"
    f"{str(candidates[1])}: {str(candidates_percentage[1])}% ({str(candidates_total_votes[1])})\n"
    f"{str(candidates[2])}: {str(candidates_percentage[2])}% ({str(candidates_total_votes[2])})\n"
    f"{str(candidates[3])}: {str(candidates_percentage[3])}% ({str(candidates_total_votes[3])})\n"
    f"------------------------\n"
    f"Winner: {election_winner}\n"
    f"------------------------\n"
)

print(output)

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------