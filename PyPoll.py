# Add our dependencies
import csv
import os
from wsgiref.headers import Headers
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to save the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load,'r',encoding='utf_8') as election_data:
# To Do :  Read and analyse the data here
# Read the file object with reader function
    file_reader = csv.reader(election_data)
# Print the header row
    headers = next(file_reader)
    print(headers)



# Close the file