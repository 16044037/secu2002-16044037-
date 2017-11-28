#Task 5

import pickle
# This then allows us to load the stored data
fname = 'shapeshift.p'
X=pickle.load(open(fname, 'rb'))

# I used this to print out all 50 transactions into an easily readable format
for i in range(0,len(X)):
    print X[i]

print '--------------------------------------------------------------'
# We want to find out how many transactions have Ethereum (ETH) as the input currency
# To do this easily we can use filter and lambda
# Any transactions that are equal to the specified names will be counted
ETH = filter(lambda x: x["curIn"] == "ETH", X)
print 'ETH'
print 'There are', len(ETH), 'transactions that have ETH as the input currency'

print '--------------------------------------------------------------'

# We want to find out how many transactions have Bitcoin 'BTC' as the output currency
# Again, we can use filter and lambda
# Any transactions that are equal to the specified names will be counted
BTC = filter(lambda x: x["curOut"] == 'BTC', X)
print 'BTC'
print 'There are', len(BTC), 'transactions that have BTC as the output currency'

print '--------------------------------------------------------------'

# We want to find out how many transactions include the trading of Zcash (ZEC) to Bitcoin
# Again, we can use filter and lambda
# Any transactions that are equal to the specified names will be counted
ZEC = filter(lambda x: x["curIn"] == 'ZEC' and ["curOut"] == 'BTC', X)
print 'ZEC to BTC'
print 'There are', len(ZEC), 'transactions involving the trading of ZEC to Bitcoin'

print '----------------------------------------------------------------'

