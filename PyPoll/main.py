import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votescast = [] 
candidates = []
candidates_list = []
votes = []
total_candidate_votes = []


with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

# Loop through data
    for row in csvread:

# The total number of votes cast
        votescast.append(row[0])
        totalvotes = len(votescast)

# Add candidates name to list
        candidates.append(row[2])

print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(totalvotes))
print("-----------------------------------")
 
for x in candidates:
    if x not in candidates_list:
        candidates_list.append(x)
        votes_each_candidate = candidates.count((candidates_list[-1])) 
        votes_each_candidate = candidates.count((candidates_list[-1])) 
        votes.append(int(votes_each_candidate))

        percent_each=((votes_each_candidate/totalvotes)*100)
        percent_each=round(percent_each, 4)

        total_candidate_votes.append(int(percent_each))
        vote_total_each = max(total_candidate_votes)
        vote_index  = total_candidate_votes.index(vote_total_each)
        
        winner = candidates_list[vote_index]
    
        print(candidates_list[-1] + ': ' + str(percent_each) + '% ' + '(' + str(votes_each_candidate) + ')')
print("-----------------------------------")
print('Winner: ' + winner)     

# Specify the file to write to
output_path = os.path.join("..", "Resources", "electiondata.txt")

# Open the file using "write" mode. Specify the variable f to hold the contents
with open(output_path, 'w') as f:
        f.write("Election Results\n")
        f.write("-----------------------------------\n")
        f.write("Total Votes: " + str(totalvotes) + "\n")
        f.write("-----------------------------------\n")
        for x in candidates_list:
                f.write(candidates_list[-1] + ': ' + str(percent_each) + '% ' + '(' + str(votes_each_candidate) + ')'+ "\n")
        f.write("-----------------------------------\n")
        f.write('Winner: ' + winner)