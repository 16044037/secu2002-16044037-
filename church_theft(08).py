# Task 5
# Firstly, we need to open the file we want to work with and read it...
f = open('/Users/paige/secu2002_master/data/church_metal_theft.csv','r')

# Firstly we need to copy over the solutions from Lab04 and 05 which are shown below...
# CREATE_ROW: used to create dict-style row for spreadsheet
# input:    columns (as list)
# output:   row (as dict)
def create_row(columns):
    # columns are: (0) start date,
    #              (1) start time,
    #              (2) end date,
    #              (3) end time,
    #              (4) free text
    d = {'start date' : columns[0], 'start time' : columns[1],
         'end date' : columns[2], 'end time' : columns[3],
         'text' : columns[4]}
    return d

# GET_PRETTY_MONTH: used to map month number to word
# input:    months (as list of ints)
# output:   months (as list of strings)
def pretty_month(months):
    d = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    pretty_months = []
    for m in months:
        if m in d:
            pretty_months.append(d[m])
        else:
            print 'entered an invalid month'
            return
    return pretty_months

# this is a fancy way to create a dictionary with months as keys, 0 as value
months = dict.fromkeys(range(1,13),0)

# This allows us to parse lines into a spreadsheet-type format
spreadsheet = []
import csv
# We then use csv.DictReader
# This has the same functionality as if we used dictionaries to map the column's meaning to its value
# We also want to use'|' as the delimiter between columns rather than ':::'
r = csv.DictReader(f, delimiter='|')
# We then want to append these labels to the spreadsheet permanently
for row in r:
   spreadsheet.append(row)
print spreadsheet

# Example of a list comprehension: get just text field from crime data
# Use lower to ensure consistency across all entries
texts = [x['text'].lower() for x in spreadsheet]

print '-----------------------------------'
# All crimes involving lead using lambda
lead = filter(lambda x : 'lead' in x, texts)
print 'LEAD'
print 'There are', len(lead), 'crimes involving lead'
print '-----------------------------------'

# All crimes involving copper using lambda
copper = filter(lambda x : 'copper' in x, texts)
print 'COPPER'
print 'There are', len(copper), 'crimes involving copper'
print '-----------------------------------'

# This is the total number of crimes
total_crimes = size = len(texts)
print 'There are', total_crimes, 'crimes in total'
print '-----------------------------------'

# Now go through crimes and put them into month and season buckets
for row in spreadsheet:
    # Could also work according to end date
    start_date = row['start date']
    # Date is as dd/mm/yyyy
    split_date = start_date.split('/')
    month = int(split_date[1])
    # Count entry in both month it occurred
    months[month] += 1

print 'These are the crimes in each month', months
print '-----------------------------------'

# By using this for loop, for every crime that involves lead, it will print us the date at which this occurred
LEAD = []
for x in spreadsheet:
    for i in x:
        if i == 'text':
            if 'lead' in x[i].lower():
                LEAD.append(x['start date'])
print LEAD
print '-----------------------------------'

# By using this for loop, for every crime that involves copper, it will print us the date at which this occurred
COPPER = []
for x in spreadsheet:
    for i in x:
        if i == 'text':
            if 'copper' in x[i].lower():
                COPPER.append(x['start date'])
print COPPER
print '-----------------------------------'

# We then want to create an empty dictionary for both Lead and Copper
# This means that we can use a for loop to add to the dictionary every time a month where a lead or copper theft has taken place
LEAD_months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0,
                'September': 0, 'October': 0,'November': 0, 'December': 0}
COPPER_months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0,
                'September': 0, 'October': 0,'November': 0, 'December': 0}

# Although it is not elegant, it does the job
# This will be printed out for all months for both Lead and Copper
for x in range (0,len(LEAD)):
    # The indexing here is used to locate the numbers in which the months will be situated in the start date
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='1':
                # For every start date of a crime which has 01, we want to count 1 towards January
                # This is the case with the rest of them
                LEAD_months['January'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='2':
                LEAD_months['February'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='3':
                LEAD_months['March'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='4':
                LEAD_months['April'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='5':
                LEAD_months['May'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='6':
                LEAD_months['June'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='7':
                LEAD_months['July'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months =='0' and months2 =='8':
                LEAD_months['August'] += 1

for x in range(0, len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][4]:
            if months == '0' and months2 == '9':
                LEAD_months['September'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][3 and 4]:
            if months =='1' and months2 =='0':
                LEAD_months['October'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][3 and 4]:
            if months =='1' and months2 =='1':
                LEAD_months['November'] += 1

for x in range (0,len(LEAD)):
    for months in LEAD[x][3]:
        for months2 in LEAD[x][3 and 4]:
            if months =='1' and months2 =='2':
                LEAD_months['December'] += 1

# This will then print an update dictionary of months involving thefts of lead
print LEAD_months
print '-----------------------------------'

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='1':
                COPPER_months['January'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='2':
                COPPER_months['February'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='3':
                COPPER_months['March'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='4':
                COPPER_months['April'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='5':
                COPPER_months['May'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='6':
                COPPER_months['June'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='7':
                COPPER_months['July'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months =='0' and months2 =='8':
                COPPER_months['August'] += 1

for x in range(0, len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][4]:
            if months == '0' and months2 == '9':
                COPPER_months['September'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][3 and 4]:
            if months =='1' and months2 =='0':
                COPPER_months['October'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][3 and 4]:
            if months =='1' and months2 =='1':
                COPPER_months['November'] += 1

for x in range (0,len(COPPER)):
    for months in COPPER[x][3]:
        for months2 in COPPER[x][3 and 4]:
            if months == '1' and months2 == '2':
                COPPER_months['December'] += 1

# This will then print an update dictionary of months involving thefts of copper
print COPPER_months

# We then want to use all of this information to plot onto a clustered bar chart
# Thus, firstly we need to import matplotlib which is the core graphing package for Python
import matplotlib.pyplot as plt

# Our x axis wants to be the months in which the crimes occurred
xaxis = ['January','February','March','April','May','June','July','August','September','October','November','December']
# This is the data from the COPPER_months dictionary
yaxis_copper = [0,0,5,2,2,1,4,3,4,1,1,1]
# This is the data from the LEAD_months dictionary
yaxis_lead = [6,10,6,14,5,3,7,13,8,8,11,2]
# This is the data from the months dictionary with all crimes documented in each month
yaxis_total = [7,11,11,19,8,5,13,18,12,9,12,5]
# We then want to plot these three bars as such, and making adjustments for aesthetic reasons
plt.bar(map(lambda x: x + 0.3, range(len(xaxis))), yaxis_copper, align='center', color='b', width=0.3, label='Number of copper thefts')
plt.bar(map(lambda x: x + 0.1, range(len(xaxis))), yaxis_lead, align='center', color='r', width=0.3, label='Number of lead thefts')
plt.bar(map(lambda x: x - 0.2, range(len(xaxis))), yaxis_total, align='center', color='g', width=0.3, label='Total number of crimes')
# This is then our x axis label
plt.xlabel('Months', fontsize=7)
# This then plots each month along the x axis
plt.xticks(range(len(xaxis)), xaxis, fontsize=7, rotation=50)
# This tells us what the y axis is for
plt.ylabel('Number of crimes', fontsize=7)
# This plots us our legend
plt.legend(loc='best', fontsize=7)
# This is the title of the bar chart
plt.title('Number of lead thefts, copper thefts, and the total number of crimes that occurred in each month', fontsize=7)
# And this is how we save it!
plt.savefig('months.pdf')