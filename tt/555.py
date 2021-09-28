# -*- coding: utf-8



# 7 fun(*args,**kwargs)中的*args,**kwargs什么意思？
def test(one,*two):
    print(one)
    print(two)
    print (type(two))
    pass

list33=[1,2,3]
test(1,*list33)

def test2(**kwargs):

    print(kwargs)
dict2 ={"join":33}
test2(join=33,jay=44)
test2(**dict2)#传入dict需要加上**

import os
# import json
import sys
import datetime
import math
import re
import threading

