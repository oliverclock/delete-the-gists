#install simplegist, i.e. pip install simplegist
from simplegist import Simplegist
#get a personal token for gist from github.com, use your username and token here
GHgist = Simplegist(username='your_username',api_token='your_token')
list = GHgist.search('your_usernamek').listall()
for line in list: 
    print line
    GHgist.profile().delete(name=line)
    print '..Deleted!'
print 'Done'   
