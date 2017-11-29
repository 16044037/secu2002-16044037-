#Task 5

# We need to import the requests module to get the information we need
import requests
# In particular we need the 50 most recent ShapeShift transactions
# We also want to name the command of requesting this to use later
transaction_file = requests.get('https://shapeshift.io/recenttx/50')
# And we want to store this data using a meaningful variable 'transactions'
transactions = transaction_file.json()

# For the next part we want to import the pickle module
# This allows us to keep data structures intact when saving to a file
import pickle

# This then stores this the information we want intact in a specified file
transactions_pickle = 'shapeshift.p'
shapeshift = pickle.dump(transactions, open(transactions_pickle, 'wb'))


