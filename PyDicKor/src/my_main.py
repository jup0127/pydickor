'''
Created on 2014. 4. 24.

@author: MY
'''
import sys
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("localhost", 9000)
    
    db = client.test
    
    users = db.users
    
    doc = {'_id' : 'myid', 'firstname' : 'Terry', 'lastname' : 'L'}
    
    try:
        users.insert(doc)
    except:
        print "insert_failed", sys.exc_info()[0]
    
    print db.name