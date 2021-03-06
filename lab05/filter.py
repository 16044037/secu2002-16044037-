#Task 1

#Firstly, it is important to define a list as shown below
mylist=[3,13,23,33,43]
#We are then assigning the variable 'n' to the value of 23
n = 23

#LOOP_FILTER: when given a numeric list (mylist) and a number (n), returns the numbers in the list that are greater than n
#Input: a list (mylist), i which represents the values in the list, and a value to filter it against (n)
#Output: elements of the list that are greater than the value of n
def loop_filter(mylist, n):
    for i in mylist:
        if i > n:
            print i
    return i > n

loop_filter(mylist, n)

print '------------'

#Task 2

#Here we want to use lambda to filter instead of defining a function to do so
#I want to store the new list as the filtered list and so I have used a statement to do this
#I am inputting a list (mylist) and a number (n)
#By using their names rather than the values assigned to the names, it means that it can be used in various examples instead of being specific to just one
#This means that I can change the value of mylist and n and still get the correct result (as shown in a second example below)
mylist=filter(lambda x : x > n, mylist)
#This will then test whether the new list has been sucessfully stored
#It will also test whether the filter function has worked correctly
print 'This should return 33 and 43'
print 'Is returning\t',mylist

print '------------'

#Example 2
mylist=[4,5,6,7,8]
n = 6

mylist=filter(lambda x : x > n, mylist)

print 'This should return 7 and 8'
print 'Is returning\t',mylist

