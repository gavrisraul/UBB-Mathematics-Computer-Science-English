#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
logic module
see pdf for requirements
"""

l = [(1, "a", 2)]

def printAllStudents(myLst):
    s=" "
    for x in myLst:
        s=s+str(x[0])+" "+x[1]+" has grade "+str(x[2])+"\n"
    return s[:len(s)-1]

def findById(l, id):
    for i in range(0, len(l)):
        if l[i][0]==id:
            return i
    return True

def addStudent(l,el):
    if findById(l,el[0]) != True:
        return False
    l.append(el)

def deleteById(l,id):
    c=findById(l,id)
    if c != True:
        del l[c]
        return True
    return False

def getGradesGreater(l,n):
    great_list = []
    for el in l:
        if el[2]>n:
            great_list.append(el)
    return great_list

def getMaxGrade(l):
    mx = (-1," ",-1)
    for el in l:
        if el[2]>mx[2]:
            mx = el
    return mx

def StudentToString(student):
    return str(student[0])+" "+student[1]+" "+str(student[2])

def FindByName(lst, name):
    ls = []
    for i in range(0, len(lst)):
        if name in lst[i][1]:
            ls.append(lst[i])
    return ls

def FindByGradeLessThan(lst, grade):
    ltoremove = []
    for i in range(0, len(lst)):
        if lst[i][2] < grade:
            ltoremove.append(lst[i])
    return ltoremove

def IsPalindrome(elem):
    if elem[:] == elem[::-1]:
        return True
    return False

def GetFrq(lst, name):
    frq = 0
    for i in range(0, len(lst)):
        if lst[i][1] == name:
            frq += 1
    return frq

def GetAverageGreaterThan5(lst):
    s = 0
    j = 0
    for i in range(0, len(l)):
        if l[i][2] >= 5:
            s += l[i][2]
            j += 1
    return float(s/j)

def SortByGrade(lst):
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][2] < lst[j][2]:
                aux = lst[i]
                lst[i] = lst[j]
                lst[j] = aux
    return lst

def FindTop3(lst):
    ls = []
    sort = SortByGrade(lst)
    for i in range(0, len(sort)):
        if i == 3:
            break
        ls.append(sort[i])
    return ls

