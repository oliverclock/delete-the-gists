#install simplegist, i.e. pip install simplegist
from simplegist import Simplegist
#get a personal token for gist from github.com, use your username and token here
GHgist = Simplegist(username='oliverclock',api_token='58ef0133e2096c774e8be7f4e1f836f8f68a7508')
list = GHgist.search('oliverclock').listall()
for line in list: 
    print line
    GHgist.profile().delete(name=line)
    print '..Deleted!'
print 'Done'   