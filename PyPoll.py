# Add our dependencies
import csv
import os
from wsgiref.headers import Headers
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to save the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Initialize candidate option
candidate_options=[]
# Initialize candidate_votes dictionary and declare it empty
candidate_votes = {}
# Winning Candidate and winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
# Open the election results and read the file
with open(file_to_load,'r',encoding='utf_8') as election_data:
# To Do :  Read and analyse the data here
# Read the file object with reader function
    file_reader = csv.reader(election_data)
# Read the header row
    headers = next(file_reader)
# Print each row in CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...  
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidates list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's vote
        candidate_votes[candidate_name] +=1
# Determine the percentage of votes for each candidate by looping through the counts
# 1.Iterate through candidate list
for candidate_name in candidate_votes :
    # 2. Retreive vote count of candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100 
    # Print Candidate name with percentage of votes
    print(f"{candidate_name} : received {vote_percentage:.1f} % ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than winning count
    if (votes > winning_count) and (vote_percentage>winning_percentage):
        # If true, then set winning count = votes and winning percentage = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning candidate equal to candidate's name
        winning_candidate = candidate_name
        # Print the winning candidate, votecount and vote percentage
winning_candidate_summary = (f"-------------------------\n"
                             f"Winner: {winning_candidate}\n"
                             f"Winning vote count: {winning_count:,}\n"
                             f"Winning Percentage: {winning_percentage:.1f}%\n"
                             f"--------------------------\n")
print(winning_candidate_summary)




# Close the file