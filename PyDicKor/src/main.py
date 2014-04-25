'''
Created on 2014. 4. 18.

@author: My
'''
from pydickor import *


if __name__ == '__main__':
    my_py_dic_kor = PyDicKor(raw_input("pass_phrase : "))
    print my_py_dic_kor.getUserIdHash()