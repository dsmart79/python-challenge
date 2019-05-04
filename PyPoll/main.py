# Import modules
import os
import csv

# Set path
py_poll_data = os.path.join("../PyPoll", "election_data.csv")

# Setting initial vote count and naming lists
total_votes = 0
candidates_list = []
candidate = []
vote_count = []
vote_percent = []

# Open CSV
with open(py_poll_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)

    for row in csvreader:
        # Counting of total votes
        total_votes += 1
        
        # Appending candidates_list to store names of candidates
        if len(row) == 3:
            candidates_list.append(row[2])
    
    # Set is created to get individual candidate names
    for name in set(candidates_list): 
        
        candidate.append(name)
        
        votes_per_candidate = candidates_list.count(name)
        
        vote_count.append(votes_per_candidate)
        
        percent_votes = (votes_per_candidate/total_votes) * 100
        
        vote_percent.append(percent_votes)

    winning_vote_number = max(vote_count)
    
    winner = candidate[vote_count.index(winning_vote_number)]

print("-------------------------------------")
print("Election Results")   
print("-------------------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------------------")
print("The winner is: " + winner +"!")
print("-------------------------------------")

with open("election_output.txt", "w") as text:
    text.write("-------------------------------------\n")
    text.write("Election Results" + "\n")   
    text.write("-------------------------------------\n")
    text.write("Total Votes :" + str(total_votes) + "\n")    
    text.write("-------------------------------------\n")
    for i in range(len(candidate)):
                text.write(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")" + "\n")
    text.write("-------------------------------------\n")
    text.write("The winner is: " + winner +"!" + "\n")
    text.write("-------------------------------------\n")