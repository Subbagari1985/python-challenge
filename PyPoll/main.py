import os
import csv
import pandas as pd

datapath = os.path.join('Resources','election_data.csv')

#Opening the file
with open (datapath) as election_data_file:
    #Moving to the next line since there are headers in the csv provided
    #next(election_data_file)
    #Reading from the csv file
    csv_reader = csv.DictReader(election_data_file, delimiter=",")
    count = 0
    Candidate = []
    #Assigning the list from the csv to the variable data
    data = list(csv_reader)
#Calculating total number of Votes in the csv provided
    Total_Votes = len(data)
    print("Election Results")
    print("----------------------------------")
    print("Total Votes:  " + str(Total_Votes))
    print("----------------------------------")
   
 # read specific columns of csv file using Pandas
df = pd.read_csv(datapath, usecols = ['Voter ID','County','Candidate'])
unique_Candidates = df['Candidate'].unique()
#print(unique_Candidates[1])
#print("-------------------------------------------------")
Number_Votes_Candidates = pd.value_counts(df['Candidate'].values)
#print(Number_Votes_Candidates[1])
#print("-------------------------------------------------")
for each in unique_Candidates:
    percentages= (Number_Votes_Candidates/Total_Votes)*100
#print(percentages[1])
print(unique_Candidates[0] +":   "+str(round(percentages[0],4))+"%    ("+str(Number_Votes_Candidates[0])+")")
print(unique_Candidates[1] +":   "+str(round(percentages[1],4))+"%    ("+str(Number_Votes_Candidates[1])+")")
print(unique_Candidates[2] +":   "+str(round(percentages[2],4))+"%    ("+str(Number_Votes_Candidates[2])+")")
print(unique_Candidates[3] +":   "+str(round(percentages[3],4))+"%    ("+str(Number_Votes_Candidates[3])+")")

result={"Percentages":round(percentages,4),"Votes":Number_Votes_Candidates, "Candidate":unique_Candidates}
result_df=pd.DataFrame(result)
result_df = result_df.set_index(round(percentages,4))
#print(result_df)
Winner=round(percentages.max(), 4)
#print(Winner)
winner_name= result_df.loc[Winner,"Candidate"]
print("----------------------------------")
print("Winner:  "+winner_name)
print("----------------------------------")



#dict={'Candidate':'List_Candidates[0]','Votes':'List_Candidates[1]'}
#result_df=pd.DataFrame('Candidate':'List_Candidates[0]','Votes':'List_Candidates[1]')
#print(result_df)
    
#Calculating the total number of
    #FOr each row in the list "data", convering values into Integer and adding using Sum function.
   
  
  


