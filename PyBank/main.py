import os
import csv

#create the path for election_data.csv

data_path= os.path.join('Resources','budget_data.csv')

# create list for month, profit, and profit change
month = []
profit = []
profit_change = []
# set initial value of total = 0, total_profit_change = 0, greatest_profit = 0, greatest_loss = 0
total = 0
total_profit_change = 0
greatest_profit = 0
greatest_loss = 0

#read the csv data
with open(data_path, newline = '') as data_file:
    csvreader = csv.reader(data_file, delimiter = ',')
    #remove the header
    csv_header = next(csvreader)
    #add month and profit/loss to month and profit_loss list
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))

#total month
total_month = len(month)

#calculating total profit
for p in profit:
    total += p    

#calculating profit change for each month
for i in range(len(profit)-1):
    profit_change.append(profit[i+1]-profit[i])

#calculating average change
for pc in profit_change:
    total_profit_change += pc

average_change = total_profit_change/len(profit_change)

#calculating the greatest profit
for j in range(len(profit_change)):
    if profit_change[j] > 0:
        if profit_change[j] > greatest_profit:
            greatest_profit = profit_change[j]
            k = j 
          

#calculating the greatest loss
for m in range(len(profit_change)):
    if profit_change[m] < 0:
        if profit_change[m] < greatest_loss:
            greatest_loss = profit_change[m]
            n = m 
    


print('Finanical Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {month[k+1]} (${profit_change[k]})')
print(f'Greatest Decrease in Profits: {month[n+1]} (${profit_change[n]})')


#writing data into pybank_summary.txt

output = 'pybank_summary.txt'

with open(output, 'w') as txtfile:
    txtfile.write('Finanical Analysis \n')
    txtfile.write('---------------------------- \n')
    txtfile.write(f'Total Months: {total_month} \n')
    txtfile.write(f'Total: ${total} \n')     
    txtfile.write(f'Average Change: ${round(average_change, 2)} \n')
    txtfile.write(f'Greatest Increase in Profits: {month[k+1]} (${profit_change[k]}) \n')
    txtfile.write(f'Greatest Decrease in Profits: {month[n+1]} (${profit_change[n]})')