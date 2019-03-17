#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
By index
del myList[1]
del myList[1:3]
myList[1:3] = []
By element
myList.remove()


result = [x for x in mylist if x%2==0]

1 2 4 5 6 4 8 1 => 6 4 8 1 2 4 5 1
mylist[:0]=[6,4,8]
"""

def printList(myLst):
    s=" "
    for x in myLst:
        s=s+str(x)+"-"
    print(s[:len(s)-1])

def isPowerOfTwo(x):
    while x%2 == 0:
        x//=2
    if x==1:
        return True
    return False

def SumPowerOfTwo(myLst):
    s=0
    for x in myLst:
        if isPowerOfTwo(x) == True:
            s+=x
    return s

def listNotPowerOfTwo(myLst):
    s=[]
    for x in myLst:
        if isPowerOfTwo(x) == False:
            s.append(x)
    return s

def DeleteFirstAndLastEvenNr(myLst):
    for i in range(0, len(myLst)):
        if myLst[i] % 2 == 0:
            del(myLst[i])
            break
    for j in range(len(myLst)-1, 0, -1):
        if myLst[j] % 2 == 0:
            del(myLst[j])
            break
    return myLst

def DeleteAllPowerOfTwo(myLst):
    i = 0
    while i < len(myLst):
        if isPowerOfTwo(myLst[i]) == True:
            del (myLst[i])
        else:
            i += 1
    return myLst

def DeleteFromList(myLst):
    indexes = []
    for i in range(len(myLst)):
        if isPowerOfTwo(myLst[i]):
            indexes.append(i)
    for x in reversed(indexes):
        del myLst[x]
    return myLst

def ShiftSequence(myLst):
    StartPos = 0
    maxSeq=[]
    currentSeq=[]
    for index in range(len(myLst)):
        if myList[index]%2==0:
            currentSeq.append(myLst[index])
        else:
            if len(currentSeq)>len(maxSeq):
                maxSeq=currentSeq[:]
                StartPos=index-len(currentSeq)
            currentSeq=[]
    del(myLst[StartPos:StartPos+len(maxSeq)])
    myLst[:0]=maxSeq
    return myLst



myList=[]
myList.append(5)
myList.append(2)
myList.append(4)
myList.append(7)
myList.append(6)
myList.append(8)
myList.append(4)
myList.append(3)
print(myList)
#print(SumPowerOfTwo(myList))
#print(listNotPowerOfTwo(myList))
#print(DeleteFirstAndLastEvenNr(myList))
#print(DeleteFromList(myList))
print(ShiftSequence(myList))
