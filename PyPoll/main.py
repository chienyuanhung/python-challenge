import os
import csv

data_path= os.path.join('Resources','election_data.csv')

candidate_list = []
results = {}

#read the csv data and get candidate list
with open(data_path, newline = '') as data_file:
    csvreader = csv.reader(data_file, delimiter = ',')
    #remove the header
    csv_header = next(csvreader)
    #get the candidate_list
    for row in csvreader:
        if not row[2] in candidate_list:
            candidate_list.append(row[2])

#create dictioary for results
for candidate in candidate_list:
    results[candidate] = 0

#count the ballot

with open(data_path, newline = '') as data_file:
    csvreader = csv.reader(data_file, delimiter = ',')
    #remove the header
    csv_header = next(csvreader)
    for row in csvreader:
        candidate = row[2]
        results[candidate] +=1

#get total ballots
total_votes = 0
for count in results.values():
    total_votes += count

#get winner's name
winner_count = 0

for name, count in zip(results.keys(), results.values()):
    if count > winner_count:
        winner_count = count
        winner_name = name

#print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for name, count in zip(results.keys(), results.values()):
    print(f'{name}: {(round(100*(count/total_votes), 3))}% {count}')
print('-------------------------')
print(f'Winner: {winner_name}')
print('-------------------------')

#write results into pypoll_summary.txt
output = 'pypoll_summary.txt'

with open(output, 'w') as txtfile:
    txtfile.write('Election Results \n')
    txtfile.write('------------------------- \n')
    txtfile.write(f'Total Votes: {total_votes} \n')
    txtfile.write('------------------------- \n')
    for name, count in zip(results.keys(), results.values()):
        txtfile.write(f'{name}: {(round(100*(count/total_votes), 3))}% {count} \n') 
    txtfile.write('------------------------- \n')    
    txtfile.write(f'Winner: {winner_name} \n')
    txtfile.write('-------------------------')
    