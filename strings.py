#Task 1

#Example 1 of the string mysep.join(mylist)
#Define my list with a list of colours
mylist = ['blue', 'pink', 'purple', 'red', 'green']
#Define a separator as a space
mysep = ' '
print 'should return: blue pink purple red green'
print 'is returning', mysep.join(mylist)
print '-------------'

#Example 2 of the string mysep.join(mylist)
#Define my list with a list of foods
mylist = ['crisps','chocolate','biscuits','cereal','soup']
#Define a separator as a space
mysep = ' '
print 'should return: crisps chocolate biscuits cereal soup'
print 'is returning', mysep.join(mylist)
print '-------------'

#MYJOIN: joins together mylist and mysep using i and mystr
#input: list (my_list) and a separator (mysep)
#output: mylist and mysep joined together

my_list = ['a','b','c','d']
mysep = ' '
print mysep.join(my_list)

print '-------------'

def my_join(my_list,mysep):
    mystr = ''
    for i in my_list:
        mystr += i+mysep
    mystr=mystr[:-1]
    return mystr

print my_join(my_list,mysep)

print '-------------'

#Task 2

#SORT_STRING: alphabetically sort a string
#input: a string (mystr) and a separator (mysep)
#output: an alphabetically sorted string of letters

mystr = ['b','e','a','d','c']

def sort_string(mystr):
    mysep = ' '
    L = list(mystr)
    L.sort()
    mystr = mysep.join(L)
    return mystr

print sort_string(mystr)

print '-------------'





