import os
import csv
import pandas as pd

#Path to the csv file
datapath = os.path.join('Resources','election_data.csv')

#Opening the file
with open (datapath) as election_data_file:
    
    #Reading from the csv file
    csv_reader = csv.DictReader(election_data_file, delimiter=",")
    
    #Assigning the list from the csv to the variable data
    data = list(csv_reader)
#Calculating total number of Votes in the csv provided
    Total_Votes = len(data)
       
 # read specific columns of csv file using Pandas
df = pd.read_csv(datapath, usecols = ['Voter ID','County','Candidate'])

#List of Candidates participated in the election
unique_Candidates = df['Candidate'].unique()

#Calculating Number of Votes for each candidate in the election
Number_Votes_Candidates = pd.value_counts(df['Candidate'].values)

#Calculating Percentages of Votes received for each candidate.
for each in unique_Candidates:
    percentages= (Number_Votes_Candidates/Total_Votes)*100

#Creating a DataFrame to access information
result={"Percentages":round(percentages,4),"Votes":Number_Votes_Candidates, "Candidate":unique_Candidates}
result_df=pd.DataFrame(result)
result_df = result_df.set_index(round(percentages,4))

#Calculating who won the election using Loc and Dataframe
Winner=round(percentages.max(), 4)
winner_name= result_df.loc[Winner,"Candidate"]

#Writing Output to text file
with open("Analysis\PyPoll_Output_textfile.txt", 'x') as f:
    
    f.write("Election Results"+'\n')
    f.write("----------------------------------"+'\n')
    f.write("Total Votes:  " + str(Total_Votes)+'\n')
    f.write("----------------------------------"+'\n')

    f.write(unique_Candidates[0] +":   "+str(round(percentages[0],4))+"%    ("+str(Number_Votes_Candidates[0])+")"+'\n')
    f.write(unique_Candidates[1] +":   "+str(round(percentages[1],4))+"%    ("+str(Number_Votes_Candidates[1])+")"+'\n')
    f.write(unique_Candidates[2] +":   "+str(round(percentages[2],4))+"%    ("+str(Number_Votes_Candidates[2])+")"+'\n')
    f.write(unique_Candidates[3] +":   "+str(round(percentages[3],4))+"%    ("+str(Number_Votes_Candidates[3])+")"+'\n')
    f.write("----------------------------------"+'\n')
    f.write("Winner:  "+winner_name+'\n')
    f.write("----------------------------------"+'\n')  
f.close()

#Reading Output from text file
with open("Analysis\PyPoll_Output_textfile.txt", "r") as f:
	print(f.read())
  


