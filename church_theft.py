#Task 4

#Firstly, we need to open the file and display the data in a list format
f = open('/Users/paige/secu2002_-16044037-/Lab04/church_metal_theft.csv', 'r')
#This then allows us to see each row in the data as one element of the list
rows = f.readlines()

#This allows us to print an empty line between each line of data to see it more clearly
print ''
#This gets us the free text field details of the crimes that have occurred
free_text_field = []
for row in rows:
    free_text_field.append(row[48:])

#This converts all of the data into lowercase letters to standardise the data into a lowercase format
free_text_field = [x.lower() for x in free_text_field]
#We can see this by printing the free text field out
print "The free text field details of all the thefts:", free_text_field
print '--------------'

#Using Lambda, we can filter out only the crimes that involve the theft of lead
lead_thefts = filter (lambda x: 'lead' in x, free_text_field)
#This allows us to see the number of crimes which involve the theft of lead
num_lead = len(lead_thefts)
print 'LEAD THEFTS:'
print 'The free text field details of all the lead thefts:', lead_thefts
print 'Should return the number of lead thefts as 93'
print 'Returns the number of lead thefts as:', num_lead

print '--------------'

#Using Lambda, we can filter out only the crimes that involve the theft of copper
copper_thefts = filter (lambda x: 'copper' in x, free_text_field)
#This allows us to see the number of crimes which involve the theft of copper
num_copper = len(copper_thefts)
print 'COPPER THEFTS:'
print 'The free text field details of all the copper thefts:', copper_thefts
print 'Should return the number of copper thefts as 24'
print 'Returns the number of copper thefts as:',num_copper

print '-------------'

#Using Lambda, we can filter out only the crimes that involve the theft of lead flashing
leadflashing_thefts = filter (lambda x: 'flashing' in x, lead_thefts)
#This allows us to see the number of crimes which involve the theft of lead flashing
num_leadflashing = len(leadflashing_thefts)
print 'LEAD FLASHING THEFTS:'
print 'The free text field details of all the lead flashing thefts:', leadflashing_thefts
print 'Should return the number of lead flashing thefts as 56'
print 'Returns the number of lead flashing thefts as:', num_leadflashing

print '-------------'

#Using Lambda, we can filter out only the crimes that involve the theft of parts from lead roofs
leadroof_theft = filter (lambda x: 'roof' in x, lead_thefts)
#This allows us to see the number of crimes which involve the theft of parts from lead roofs
num_leadroof = len(leadroof_theft)
print 'LEAD ROOF THEFTS:'
print 'The free text field details of all the lead roof thefts:', leadroof_theft
print 'Should return the number of parts from lead roof thefts as 85'
print 'Returns the number of parts from lead roof thefts as', num_leadroof

print '-------------'

#To find the number of crimes which involve neither the theft of lead flashing or theft of part from lead roofs, we need to create sets
#Set 1 states the number of lead thefts across the board
s1 = set(lead_thefts)
#Set 2 is the number of thefts of lead flashing
s2 = set(leadflashing_thefts)
#Set 3 is the number of thefts which involve the thefts of parts of lead roofs
s3 = set(leadroof_theft)

#We need to create a set union to join together the thefts of lead flashing and parts of lead roofs
s4 = set(leadflashing_thefts) | set(leadroof_theft)

#In order to find the number of crimes which involve neither of those, we need to find the difference between the set union and the number of thefts in general
s1.difference(s4)
difference = len(s1.difference(s4))
print 'CRIMES THAT INVOLVE NEITHER THE THEFT OF LEAD FLASHING OR THEFT OF PARTS FROM LEAD ROOFS:'
print 'Should return the number of thefts as 4'
print 'Returns the number of thefts as:', difference

print '-------------'

#Using Lambda, we are trying to find the thefts that involve stealing lead from roofs in the whole data set
leadroof_theft = filter (lambda x: 'roof' in x, free_text_field)
#This will tell us the number of thefts of parts from lead roofs
num_leadroof_details = len(leadroof_theft)
print 'THEFTS OF PARTS FROM LEAD ROOFS IN WHOLE DATASET:'
print 'The free text field details of all the lead roof thefts:', leadroof_theft
print 'Should return the number of lead roof thefts as 94'
print 'Returns the number of lead roof thefts as:', num_leadroof_details

#The problem here is that when searching for thefts that involve stealing parts of a lead roof in the dataset, the number is higher than the number of lead thefts across the whole dataset
#This is because it includes attempted thefts

print '----------'

#Here we are trying to find out the number of copper thefts which involve the theft of a lightning rod
#When manually inspecting the data set, although the spelling of 'lightening' is different, it is always followed by either 'rod', 'rods, 'conductor', or 'conducter'
#So, it makes more sense to look for these variations instead
copper_lightningrod = filter(lambda x: 'rod'in x or 'rods' in x or 'conductor' in x or 'conducter' in x, copper_thefts)
#This tells us the number of thefts of copper which involve the thefts of lightning rods, despite the variations above
num_copper_lightningrod = len(copper_lightningrod)
print 'COPPER LIGHTNING ROD THEFTS:'
print 'The free text field details of all copper lightning rod thefts:', copper_lightningrod
print 'Should return the number of copper lightning rod thefts as 16'
print 'Returns the number of copper lightning rod thefts as:', num_copper_lightningrod




