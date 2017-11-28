#Task 4

# Here we are importing the requests module to get information from this Github API
# As this has JSON already built in, we do not need to import this separately
import requests
r = requests.get('https://api.github.com/repos/smeiklej/secu2002_2017/commits')
# We then want to store the list of data entries
text = r.json()
# We now have the commit messages from this API
# But we want to print out the commit messages for every commit to the master repository

# To do this we want to use a small for loop
# This includes using range and len to get all of the commits
# Here, 'i' acts as every entry
for i in range(0,len(text)):
    #This now means that we can print all of the commit messages
    print text[i]['commit']['message']

print '----------------------'

# In order to test whether this works with a different repository, I will test again using my own!
# This should now show all the commits that have been made to my own repository
r = requests.get('https://api.github.com/repos/16044037/secu2002_-16044037-/commits')
commits = r.json()

for i in range(0,len(commits)):
    print commits[i]['commit']['message']