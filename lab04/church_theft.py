#Task 5
'-*- coding: utf-8 -*-'

f = open('church_metal_theft.csv', 'r')

#Hypothesis1: Fewer crimes are commited in the winter months (December to February)
#Hypothesis2: More crimes are committed in the summer months (June to August)

#Mapping the month number to the month name

Month = [1,2,3,4,5,6,7,8,9,10,11,12]
Winter = [12,1,2]
Spring = [3,4,5]
Summer = [6,7,8]
Autumn = [9,10,11]

#Mapping the month to the season

for line in f:
    if Month in ('December','January','February'):
        season = 'Winter'
    elif Month in ('March','April','May'):
        season = 'Spring'
    elif Month in ('June','July','August'):
        season = 'Summer'
    else:
        season = 'Autumn'

#Number of crimes committed per month:

January = 7
February = 11
March = 11
April = 19
May = 8
June = 5
July = 13
August = 18
September = 12
October = 9
November = 12
December = 5

print '---------------'

#CRIME_MONTH: lets us know how many crimes were committed in a certain month
#input: month
#output: the months with their associated crime numbers

def crime_month(month):
    print 'How many crimes were committed in this month?'
    return (month)

print crime_month(January)
#Can then do the same with all the other months

#Number of crimes committed per season:

Winter = 23
Spring = 38
Summer = 36
Autumn = 33

#CRIME_SEASON: lets us know how many crimes were committed in a certain season
#input: season
#output: the seasons with their associated crime numbers

def crime_season(season):
    print 'How many crimes were committed in this season?'
    return (season)

print crime_season(Winter)
#Can do the same with the other seasons

print '---------------'

maxnum_crimes = 19
minnum_crimes = 5

minimum_number_crimes = June and December
maximum_number_crimes = April

#MAXNUMBER_CRIMES: lets us know which month had the mnost crimes
#input: the crime numbers associated with their months and the maximum number of crimes committed
#output: the month with the most crimes

def maxnumber_crimes(maxnum_crimes):
    if 7 == 19:
        print 'January had the most crimes'
    elif 11 == 19:
        print 'February had the most crimes'
    elif 11 == 19:
        print 'March had the most crimes'
    elif 19 == 19:
        print 'April had the most crimes'
    elif 8 == 19:
        print 'May had the most crimes'
    elif 5 == 19:
        print 'June had the most crimes'
    elif 13 == 19:
        print 'July had the most crimes'
    elif 18 == 19:
        print 'August had the most crimes'
    elif 12 == 19:
        print 'September had the most crimes'
    elif 9 == 19:
        print 'October had the most crimes'
    elif 12 == 19:
        print 'November had the most crimes'
    elif 5 == 19:
        print 'December had the most crimes'
    return 'Which month had the most crimes?'

maxnumber_crimes(maxnum_crimes)
#This tells us that April had the most crimes - which is correct
print '---------------'

#MINNUMBER_CRIMES: lets us know which month had the least amount of crimes
#input: the crime numbers associated with their months and the minimum number of crimes committed
#output: the month with the least amount of crimes

def minnumber_crimes(minnum_crimes):
    if 7 == 5:
        print 'January had the least amount of crimes'
    if 11 == 5:
        print 'February had the least amount of crimes'
    if 11 == 5:
        print 'March had the least amount of crimes'
    if 19 == 5:
        print 'April had the least amount of crimes'
    if 8 == 5:
        print 'May had the least amount of crimes'
    if 5 == 5:
        print 'June had the least amount of crimes'
    if 13 == 5:
        print 'July had the least amount of crimes'
    if 18 == 5:
        print 'August had the least amount of crimes'
    if 12 == 5:
        print 'September had the least amount of crimes'
    if 9 == 5:
        print 'October had the least amount of crimes'
    if 12 == 5:
        print 'November had the least amount of crimes'
    if 5 == 5:
        print 'December had the least amount of crimes'
    return 'Which month had the least amount of crimes?'

minnumber_crimes(minnum_crimes)
#This tells us that both June and December had the least amount of crimes - which is correct

#Hypothesis1 = True (23 crimes were committed in Winter in comparison to the rest)
#Hypothesis2 = False (More crimes were actually committed in Spring with 38 crimes in comparison to the rest)
