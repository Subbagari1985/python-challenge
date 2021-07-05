import os
import csv
import pandas as pd


datapath = os.path.join('Resources','budget_data.csv')
#Opening the file
with open(datapath) as budget_data_file:


    df = pd.read_csv(datapath, usecols = ['Date','Profit/Losses'])

#Calculating unique list of Months and count of Months
unique_TotalMonths = df['Date'].unique()
Number_Total_Months= pd.value_counts(unique_TotalMonths).count()

#Calculating Total Amount of Profits/Losses
Net_Total_Amount= df['Profit/Losses'].sum()
PL_Amount = df['Profit/Losses']

#Calculating the difference in Profit and Loss Amount 
Change = df['Profit/Losses'].diff()

result={"Date":unique_TotalMonths,"Profit/Losses":PL_Amount, "Difference/Change":Change}
result_df=pd.DataFrame(result)
result_df = result_df.set_index("Difference/Change")

#Calculating values using functions Max,Min,Mean and retreiving the dates using loc.
Max_Change=Change.max().__round__()
Min_Change=Change.min().__round__()
Average_Change=Change.mean().__round__(2)
Greatest_Increase_Month=result_df.loc[Max_Change,"Date"]
Greatest_Decrease_Month=result_df.loc[Min_Change,"Date"]

#Writing Output to text file and terminal
with open("PyBank_Output.txt", 'x') as f:
    
    f.write("Financial Analysis"+'\n')
    f.write("----------------------------------"+'\n')
    f.write("Total Months: " +str(Number_Total_Months)+'\n')
    f.write("Total:  $" +str(Net_Total_Amount)+'\n')
    f.write("Average Change: $" +str(Average_Change)+'\n')
    f.write("Greatest Increase in Profits:  " +Greatest_Increase_Month+ "  ($"+str(Max_Change)+")"'\n')
    f.write("Greatest Decrease in Profits:  " +Greatest_Decrease_Month+ "  ($"+str(Min_Change)+")"'\n')
f.close()

#Reading Output from text file
with open("PyBank_Output.txt", "r") as f:
	print(f.read())


