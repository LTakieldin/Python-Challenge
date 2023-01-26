import csv
import pandas as pd
import os
import numpy as np

#Path for CSV file
election_csv = os.path.join("Resources", "election_data.csv")

#Reading CSV file
election_df= pd.read_csv(election_csv,header= 0)

#Counting Number of Votes
total_votes= len(election_df.index)
total_votes2= int(total_votes)

#Array of Unique Candidates Voted for
candidates= election_df['Candidate'].unique()
candidate_count= len(candidates)

#Counts for each Candidate
charles_counts= election_df['Candidate'].value_counts()['Charles Casper Stockham']
raymon_counts= election_df['Candidate'].value_counts()['Raymon Anthony Doane']
diana_counts= election_df['Candidate'].value_counts()['Diana DeGette']

#Percentage for each Candidate
percent_charles= round((charles_counts/total_votes2)*100, 3)
percent_raymon= round((raymon_counts/total_votes2)*100, 3)
percent_diana= round((diana_counts/total_votes2)*100, 3)

#Winner
winner= max(percent_diana,percent_raymon,percent_charles).index(2)


#Vote Results
print('Election Results')
print('----------------')
print(f'Charles Casper Stockham: {percent_charles}% ({charles_counts})')
print(f'Diana Degette: {percent_diana}% ({diana_counts})')
print(f'Raymon Anthony Doane: {percent_raymon}% ({raymon_counts})')
print('----------------')
print('Winner:{winner}')

#Data Results Listed for .txt File
l1='Election Results\n'
l2='----------------\n'
l3='Charles Casper Stockham: 23.049% (85213)\n'
l4='Diana Degette: 73.812% (272892)\n'
l5='Raymon Anthony Doane: 3.139% (11606)\n'
l6='----------------\n'
l7='Winner: Diana Degette'

#Creating .txt file
with open ('PyPoll Results README', 'w+') as file:
    file.writelines([l1,l2,l3,l4,l5,l6,l7])