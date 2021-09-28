# -*- coding: utf-8
import flask
import json

# from flask import Flaskapp = Flask(__name__)@app.route('/')


# from tt.easymock import mymock
#
# mymock=mymock(cardNo="thisiscard")
# mymock.test()
#
# mymock.run()

# print(123)

from tt.objecttest import run




# def sortpat(list1):
#     llen=len(list1)
#     for i in range(llen):
#         for j in range(llen-1):
#             if(list1[j]<list1[j+1]):
#                 list1[j],list1[j+1]=list1[j+1],list1[j]
#     return list1
#
# ll=[9,5,7,6,3,4]
# print (sortpat(ll))



def quick_sort(list,i,j):
    if i>=j:
        return list
    low =i
    high=j
    prvot=list[i]

    while i<j:
        while i<j and list[j]>=prvot:
            j-=1
        list[i]=list[j]
        while i < j and list[i] <= prvot:
            i += 1
        list[j] = list[i]
    list[i]=prvot
    quick_sort(list,low,i-1)
    quick_sort(list,i+1,high)
    return list
ll=[5,7,6,3,4,9]
# ll=[9,5,7,6,3,4]
print(quick_sort(ll,0,len(ll)-1))
