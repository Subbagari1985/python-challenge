import os
import csv

datapath = os.path.join('Resources','budget_data.csv')
#Opening the file
with open (datapath) as budget_data_file:
    #Moving to the next line since there are headers in the csv provided
    next(budget_data_file)
    #Reading from the csv file
    csv_reader = csv.reader(budget_data_file, delimiter=",")
    #Assigning the list from the csv to the variable data
    data = list(csv_reader)
#Calculating total number of MOnths in the csv provided
    Total_Months = len(data)
    print(Total_Months)
    
#Calculating the net total amount of "Profit/Losses" over the entire period
    #FOr each row in the list "data", convering values into Integer and adding using Sum function.
    Net_Total_Amount = sum(int(x[1]) for x in data)
    print (str(Net_Total_Amount))
#Calculating the average of the changes in "Profit/Losses" over the entire period
    Average = Net_Total_Amount/Total_Months
    print(str(Average))

 
  


         



