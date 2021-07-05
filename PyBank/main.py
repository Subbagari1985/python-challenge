import os
import csv
import pandas as pd
from pandas.core.frame import DataFrame

datapath = os.path.join('Resources','budget_data.csv')
#Opening the file
with open(datapath) as budget_data_file:


    df = pd.read_csv(datapath, usecols = ['Date','Profit/Losses'])

#List of Candidates participated in the election
unique_TotalMonths = df['Date'].unique()
Number_Total_Months= pd.value_counts(unique_TotalMonths).count()


Net_Total_Amount= df['Profit/Losses'].sum()


PL_Amount = df['Profit/Losses']
Change = df['Profit/Losses'].diff()

result={"Date":unique_TotalMonths,"Profit/Losses":PL_Amount, "Difference/Change":Change}
result_df=pd.DataFrame(result)
result_df = result_df.set_index(Change)

Max_Change=Change.max().__round__()
Min_Change=Change.min().__round__()
Average_Change=Change.mean().__round__(2)
Greatest_Month=result_df.loc[Max_Change,"Difference/Change"]
print(Greatest_Month)

#with open("PyBank_Output.txt", 'x') as f:
    
    #f.write("Financial Analysis"+'\n')
    #f.write("----------------------------------"+'\n')
    #f.write("Total Months: " +str(Number_Total_Months)+'\n')
    #f.write("Total:  $" +str(Net_Total_Amount)+'\n')
   # f.write("Average Change: $" +str(Change.mean().__round__(2))+'\n')
  #  f.write("Greatest Increase in Profits:" +str(Change.max().__round__()+'\n'))
 #   f.write("Greatest Decrease in Profits:" +str(Change.min().__round__()+'\n'))
#f.close()
#
#Reading Output from text file#
with open("PyBank_Output.txt", "r") as f:#
	print(f.read())


