import csv
import pandas as pd
import os
import numpy as np

#Path for CSV file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Reading CSV file
budget_df= pd.read_csv(budget_data_csv,header= 0)

#Counting Number of Months
months_count= budget_df['Date'].count()

#Calculating Net Total Revenue
total_rev= budget_df['Profit/Losses'].sum()

#Retreive Changes in Profit/Losses
profit_loss_changes= list(budget_df['Profit/Losses'])
profit_loss_changes_dates= budget_df['Date']

#Variables
changes=[]
number_count=0

#Combine the Changes into Arrays
changes_in_list= np.array(profit_loss_changes)
changes_in_date= np.array(profit_loss_changes_dates)

#Using For Loop for Calculations
for change in range(len(budget_df)-1):
    first_PL= profit_loss_changes[change]
    next_PL= profit_loss_changes[change+1]
    changes.append(next_PL-first_PL)
    number_count=sum(budget_df['Profit/Losses'])
    largest_decreased_change= min(changes)
    largest_increased_change= max(changes)
    average_change= round(np.mean(changes), 2)
    largest_decreased_change_month = changes_in_date[changes.index(min(changes))+1]
    largest_increased_change_month = changes_in_date[changes.index(max(changes))+1]

#Analysis Results
print('Number of Months are:', months_count)
print('Total Revenue:',total_rev)
print('Average Change:',average_change)
print('Greatest Increase in Profits:', largest_increased_change_month, largest_increased_change)
print('Greatest Decrease in Profits:', largest_decreased_change_month, largest_decreased_change)

l1='Number of Months are: 86\n'
l2='Total Revenue: 22564198\n'
l3='Average Change: -8311.11\n'
l4='Greatest Increase in Profits: Aug-16 1862002\n'
l5='Greatest Decrease in Profits: Feb-14 -1825558\n'

#Creating .txt file
with open ('PyBank Results README', 'w+') as file:
    file.writelines([l1,l2,l3,l4,l5])

