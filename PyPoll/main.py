# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each candidate won
# 5 The winner of the election based on popular vote


# Import functions
import os
import csv
import collections
from collections import Counter

# set parameters
candidates_w_votes = []
candidate_vote_tally = []

# set path
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# open CSV and read
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # there is a header, read it
    csv_header = next(csvfile)

    # print(f"Header: {csv_header}") - code check 
    for row in csv_reader:
        candidates_w_votes.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(candidates_w_votes)

    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    candidate_vote_tally.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate
    for item in candidate_vote_tally:
       
        slot2 = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        slot1 = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        slot3 = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
          
# (ISGNORE: This was my orginal code for the export a text file and print to Git Bash"
# election_file = os.path.join("Analysis", "election_data.txt")
# with open(election_file, "w") as outfile:

#     outfile.write("Election Results\n")
#     outfile.write("-----------------------------------\n")
#     outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
#     outfile.write("-----------------------------------\n")
#     outfile.write(f"{candidate_vote_tally[0][1][0]}: {slot2}% ({candidate_vote_tally[0][1][1]})\n")
#     outfile.write(f"{candidate_vote_tally[0][0][0]}: {slot1}% ({candidate_vote_tally[0][0][1]})\n")
#     outfile.write(f"{candidate_vote_tally[0][2][0]}: {slot3}% ({candidate_vote_tally[0][2][1]})\n")
#     outfile.write("-----------------------------------\n")
#     outfile.write(f"Winner:  {candidate_vote_tally[0][0][0]}\n")
#     outfile.write("-----------------------------------\n")  

# # print to Git Bash
# print("Election Results")
# print("-----------------------------------")
# print(f"Total Votes:  {sum(count_candidate.values())}")
# print("-----------------------------------")
# print(f"{candidate_vote_tally[0][1][0]}: {slot2}% ({candidate_vote_tally[0][1][1]})")
# print(f"{candidate_vote_tally[0][0][0]}: {slot1}% ({candidate_vote_tally[0][0][1]})")
# print(f"{candidate_vote_tally[0][2][0]}: {slot3}% ({candidate_vote_tally[0][2][1]})")
# print("-----------------------------------")
# print(f"Winner:  {candidate_vote_tally[0][0][0]}")
# print("-----------------------------------")

print_path = os.path.join("Analysis", "election_data.txt")
print_path = "election_data.txt"

#UPDATED CODE: used a more efficient code posted by TA Erin Mills (thank you, Erin!)
with open(print_path, "w+") as file:
      # Message that combines multiple printed lines
    message1 = (
    f"Election Results\n"
    f"--------------------------------------------\n"
    f"Total Votes:  {sum(count_candidate.values())}\n"
    f"--------------------------------------------\n"
    f"{candidate_vote_tally[0][1][0]}: {slot2}% ({candidate_vote_tally[0][1][1]})\n"
    f"{candidate_vote_tally[0][0][0]}: {slot1}% ({candidate_vote_tally[0][0][1]})\n"
    f"{candidate_vote_tally[0][2][0]}: {slot3}% ({candidate_vote_tally[0][2][1]})\n"
    f"--------------------------------------------\n"
    f"Winner:  {candidate_vote_tally[0][0][0]}\n"
    f"--------------------------------------------\n"
    )
    print(message1)
    file.write(f"{message1}\n")
