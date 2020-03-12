# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencieis.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Inialize a total vote counter.
total_votes = 0

# Intialize total county votes.
total_county_votes = 0

# Candidate options.
candidate_options = []

# County options.
county_options = []

# Declare the empty dictionsary.
candidate_votes = {}

# Declare the empty county dictionary.
county_votes = {}

# Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning county and winning county count tracker.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
 
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        # Add to the total county vote count.
        total_county_votes += 1

        # Print the county name from each row.
        county_name = row[1]

        # If county does not match any existing county...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)      

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the candidate list.
    for county in county_votes:

        # Retrieve vote count of a candidate.
        c_votes = county_votes[county]

        # Calculate the percentage of votes.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100

        # Print the county name and percentage of votes.
        county_results = (f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        # Determine winning vote count and county.
        # Determine if the votes are greater than the winning count.
        if (c_votes > winning_county_count) and (c_vote_percentage > winning_county_percentage):

            # If true then set winning_county_count = votes and winning_percent = vote_percentage.
            winning_county_count = c_votes
            winning_county_percentage = c_vote_percentage

            # Set the winning_county equal to the candidate's name.
            winning_county = county

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes.
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote")

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    txt_file.write(winning_candidate_summary)
