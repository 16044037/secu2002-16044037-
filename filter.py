#Task 1

#Firstly, it is important to define a list as shown below
mylist=[3,13,23,33,43]
#We are then assigning the variable 'n' to the value of 23
n = 23

#We then want to define a function loop_filter, which filters the list according to the commands given
def loop_filter(mylist, n):
    for i in mylist:
        if i > n:
            print i
    return i > n

loop_filter(mylist, n)

print '------------'

#Task 2

#Here we want to use lambda to filter instead of defining a function to do so
mylist=filter(lambda x : x > 23, mylist)

print 'This should return 33 and 43'
print 'Is returning\t',mylist




