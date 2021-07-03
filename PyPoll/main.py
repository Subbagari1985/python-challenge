import os
import csv


datapath = os.path.join('Resources','election_data.csv')
#Opening the file
with open (datapath, 'r') as election_data_file:
    #Moving to the next line since there are headers in the csv provided
    next(election_data_file)
    #Reading from the csv file
    csv_reader = csv.reader(election_data_file, delimiter=",")
    #Assigning the list from the csv to the variable data
    data = list(csv_reader)
#Calculating total number of Votes in the csv provided
    Total_Votes = len(data)
    print(Total_Votes)
    
#Calculating the total number of
    #FOr each row in the list "data", convering values into Integer and adding using Sum function.
   # Total_Votes= sum(int(x[1]) for x in data)
   #
   # print (str(Net_Total_Amount))
   for row in csv_reader:
        unique_row_items = set(field.strip().lower() for field in row)
        for item in unique_row_items:
            result.add(item)
   List_Candidates= 
