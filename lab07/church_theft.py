#Task 3

# This allows us to read the contents of the selected file
f = open('/Users/paige/secu2002_master/data/church_metal_theft.csv','r')

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

