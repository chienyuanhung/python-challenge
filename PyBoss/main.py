import os
import csv


#create lists for data
emp_id = []
name = []
dob = []
ssn = []
state = []

last_name = []
first_name =[]
new_dob = []
new_ssn = []
new_state = []

new_data = []

#file name for 
file_name = ('employee_data.csv')
 
#state data
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#read the csv data
with open(file_name, newline = '') as data_file:
    csvreader = csv.reader(data_file, delimiter = ',')
    #remove the header
    csv_header = next(csvreader)
    #add month and profit/loss to month and profit_loss list
    for row in csvreader:
        emp_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])


#split name to first name and last name
for na in name:
    firstName = na.split(' ')[0]
    first_name.append(firstName)
    lastName = na.split(' ')[1]
    last_name.append(lastName)

#creat new dob

for date in dob:
    date = date.split('-')
    new_date = (f'{date[1]}/{date[2]}/{date[0]}')
    new_dob.append(new_date)

#create encrypted ssn
for n in ssn:
    n = n.split('-')
    new_n = (f'***-**-{n[2]}')
    new_ssn.append(new_n)

#crea new state list

for s in state:
    ns = us_state_abbrev[s]
    new_state.append(ns)

#assembly new data set
new_data = zip(emp_id, first_name, last_name, new_dob, new_ssn, new_state)

#write the new datafile

output_file = ('new_employee_data.csv')
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name", "Last Name","DOB", "SSN", "State"])

    writer.writerows(new_data)

