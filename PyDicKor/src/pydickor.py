'''
Created on 2014. 4. 18.

@author: My
'''
import hashlib
import sha

class PyDicKor:
    '''
    classdocs
    '''
    

    def __init__(self, user_pass_phrase):
        '''
        Constructor
        '''
        self.user_id_hash = sha.new(user_pass_phrase)
        
        
    def getUserIdHash(self):
        return self.user_id_hash