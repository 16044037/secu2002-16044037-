# Task 1

# First we import the random module as this gives us random samples to work with
import random
# We then want a random sample of 100 numbers with a range between 0 and 500
x = random.sample(range(500), 100)
y = random.sample(range(500), 100)
# This will then allows us to see these random samples
print x
print y
print '------------------'
# I will do another test with a smaller amount of numbers to test whether this is working properly
p = random.sample(range(400), 10)
z = random.sample(range(200), 20)
# And will now print to make sure I get the desired result
print p
print z
print '------------------'

# Task 2

# Hypothesis: The means of both x and y will be similar in respect to being around half of the range (500)
# First we need to import the numpy module which will help us to find the mean
import numpy as np
# This should then give us the means of both variables x and y
print 'The mean of x is', np.mean(x)
print 'The mean of y is', np.mean(y)
print '------------------'

# To make sure it is working properly, I will also test on the test variables of p and z
# Hypothesis: Again, I would expect the means to be around half of the range
print 'The mean of p is', np.mean(p)
print 'The mean of z is', np.mean(z)

print '------------------'

# Task 3

# Firstly we need to import the scipy.stats module to help us perform some statistics
# We then want to give it a shorter name 'ss' for easier coding
import scipy.stats as ss
# We then want the linear regression of variables x and y
print ss.linregress(x, y)
print '------------------'
# We also want to assign the the value of slope to the label 'slope'
slope = ss.linregress(x, y)[0]
print 'The slope is', slope
# We also want to assign the the value of intercept to the label 'slope'
intercept = ss.linregress(x, y)[1]
print 'The intercept is', intercept
print '------------------'
# As we are running the test on completely random distributions, the p-value will vary each time the test is run
# This makes it unlikely to see an indication of statistical significance, and a correlation coefficient close to 0
# This means that there will most likely be no correlation between the two variables, which is to be expected

# Task 4

# Firstly, we import matplotlib as this is the core graphing package in Python
import matplotlib.pyplot as plt
# Then, we need to create a scatter plot of our variables x and y
xaxis = x
yaxis = y
colours = []
sizes = []
for y in yaxis:
    # This lets us play with the scatter plot
    # So if the value is bigger than 250, the colour will be blue and the size will be 15
    if y > 250:
        colours.append('blue')
        sizes.append(15)
    else:
        # However, if the value is less than 250, the colour will be red, and the size will be 40
        colours.append('red')
        sizes.append(40)
plt.scatter(xaxis,yaxis,s=sizes,c=colours)
# This lets me set the limit for both the x and y axis
plt.xlim([-5,505])
plt.ylim([-5,505])
# And we then want to create a line of best fit using the equation below
xaxis = x
yaxis = [slope*x + intercept for x in xaxis]
# This lets us plot the scatter plot
plt.plot(xaxis, yaxis)
# And this lets us save the scatter plot to a pdf file
plt.savefig('scatterplot.pdf')