#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
ui module
see pdf for requirements
"""
import logic

l = [(1, "alex", 8), (2, "ana", 7), (3, "sergiu", 9), (4, "alex", 6), (5, "tudor", 5), (6, "victor", 4), (7, "abcba", 2)]


def PrintAll(myList):
    print(logic.printAllStudents(myList))


def AddNew(myList):
    idd = int(input())
    name = input()
    gr = int(input())
    logic.addStudent(myList, (idd, name, gr))


def FindStudentByID(myList):
    idd = int(input())
    return logic.findById(myList, idd) + 1


def DeleteStudentByID(myList):
    idd = int(input())
    logic.deleteById(myList, idd)


def ShowStudentsWithGradesGreater(myList):
    gr = int(input())
    print(logic.getGradesGreater(myList, gr))


def FindMaximalGrade(myList):
    print(logic.getMaxGrade(myList))


def FindStudentByName(myList):
    name = input()
    print(logic.FindByName(myList, name))


def RemoveAllWithGradeSmaller(myList):
    gr = int(input())
    print(logic.FindByGradeLessThan(myList, gr))


def DeleteIfPalindrome(myList):
    for i in range(0, len(myList)):
        if logic.IsPalindrome(myList[i][1]):
            print(myList[i])


def DetermineTheFreq(myList):
    name = input()
    frq = logic.GetFrq(myList, name)
    print(frq)


def ComputeTheAverage(myList):
    print(logic.GetAverageGreaterThan5(myList))


def SortStudentDescending(myList):
    print(logic.SortByGrade(myList))


def getTop3(myList):
    print(logic.FindTop3(myList))


def printMenu():
    s = "Menu\n"
    s += "\t1.Print all students\n"
    s += "\t2.Add a student\n"
    s += "\t3.Find a student by id\n"
    s += "\t4.Delete student by id\n"
    s += "\t5.Show students with grades greater than a given value\n"
    s += "\t6.Find a student with the maximal grade\n"
    # s+="\t7.Split the application into modules\n"
    s += "\t8.Find all students with the name starting with a given letter or substring\n"
    s += "\t9.Remove all students with the grade smaller than 5\n"
    s += "\t10.Delete students for which the first name is a palindrome\n"
    s += "\t11.Determine the frequency of a given name in student list\n"
    s += "\t12.Compute the average grade of all students having the grade higher than 5\n"
    s += "\t13.Sort students according to their grade (descending)\n"
    s += "\t14.Find the top students according to their grade (example: top 3 students)\n"
    s += "\t0.Exit\n"
    print(s)


def start():
    list = []
    n = 1
    while n != 0:
        printMenu()
        n = int(input())
        if n == 1:
            PrintAll(l)
        elif n == 2:
            AddNew(l)
        elif n == 3:
            FindStudentByID(l)
        elif n == 4:
            DeleteStudentByID(l)
        elif n == 5:
            ShowStudentsWithGradesGreater(l)
        elif n == 6:
            FindMaximalGrade(l)
        # elif n == 7:
        elif n == 8:
            FindStudentByName(l)
        elif n == 9:
            RemoveAllWithGradeSmaller(l)
        elif n == 10:
            DeleteIfPalindrome(l)
        elif n == 11:
            DetermineTheFreq(l)
        elif n == 12:
            ComputeTheAverage(l)
        elif n == 13:
            SortStudentDescending(l)
        elif n == 14:
            getTop3(l)
        elif n == 0:
            break
        else:
            print("no such option")

start()
