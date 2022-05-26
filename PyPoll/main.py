#Dependencies
import os
import csv
import math

# Specify csv path

csvpath = os.path.join("Resources","election_data.csv")

# Create the lists to store data. 

count = 0
candidate_list = []
unique_candidate = []
vote_count = []
percent_vote = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidate_list.append(row[2])
        # Create a set from the candidatelist to get the candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidate_list.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        percent_vote.append(z)

        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]


#print results to terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(percent_vote[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#print output to text file
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(percent_vote[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")