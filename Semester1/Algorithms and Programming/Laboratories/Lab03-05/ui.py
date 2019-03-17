#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
ui module for lab 3-5
see pdf for requirements
"""

import logic  # import the logic module


def Menu():  # here i print the operations that can be made
    """
    Menu
    """
    s = " "
    s += "\tadd new\n"
    s += "\tadd at last\n"
    s += "\tprint list\n"
    s += "\tremove at index\n"
    s += "\tremove at indexes\n"
    s += "\treplace\n"
    s += "\tadd at index\n"
    s += "\treplace this with this\n"
    s += "\tprint prime from to\n"
    s += "\tprint odd from to\n"
    s += "\tsum from to\n"
    s += "\tgcd from to\n"
    s += "\tmax from to\n"
    s += "\tremove nonprimes\n"
    s += "\tremove positives\n"
    s += "\tread from file\n"
    s += "\twrite to file\n"
    s += "\tundo\n"
    s += "\texit\n"
    return s


def AddOperation(myList):
    """
    AddOperation
    """
    nr = int(input("number to add to the list: "))
    logic.add_new(myList, nr)


def AddAtLast(myList):
    """
    AddAtLast
    """
    nr = int(input("number to add to the last position of the list: "))
    logic.add_at_last(myList, nr)


def PrintList(myList):
    """
    PrintList
    """
    logic.print_list(myList)


def RemoveAtIndex(myList):
    """
    RemoveAtIndex
    """
    index = int(input("the index at which you want to delete: "))
    logic.remove_at_index(myList, index)


def RemoveAtIndexes(myList):
    """
    RemoveAtIndexes
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    logic.remove_from_to(myList, index1, index2 + 1)


def Replace(myList):
    """
    Replace
    """
    nr = int(input("the number with what you want to replace: "))
    index = int(input("the index at which you want to replace: "))
    logic.replace(myList, nr, index)


def AddAtIndex(myList):
    """
    AddAtIndex
    """
    index = int(input("the index at which you want to add the number: "))
    nr = int(input("the number you want to add to the list: "))
    logic.add_at_index(myList, index, nr)


def ReplaceThisWithThis(myList):
    """
    ReplaceThisWithThis
    """
    s1 = []
    s2 = []
    n = int(input("the length of the first subseq: "))
    m = int(input("the length of the second subseq: "))
    for i in range(0, n):
        nr1 = int(input("number for the first subseq: "))
        s1.append(nr1)
    for j in range(0, m):
        nr2 = int(input("number for the second subseq: "))
        s2.append(nr2)
    logic.replace_sublist(myList, s1, s2)


def PrintPrimeFromTo(myList):
    """
    PrintPrimeFromTo
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    print(logic.PrimeFromTo(myList, index1, index2))


def PrintOddFromTo(myList):
    """
    PrintOddFromTo
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    print(logic.OddFromTo(myList, index1, index2))


def SumFromTo(myList):
    """
    SumFromTo
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    print(logic.SumFromTo(myList, index1, index2))


def GCDFromTo(myList):
    """
    GCDFromTo
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    print(logic.find_gcd(myList, index1, index2))


def MAXFromTo(myList):
    """
    MAXFromTo
    """
    index1 = int(input("index1: "))
    index2 = int(input("index2: "))
    print(logic.MaxFromTo(myList, index1, index2))


def RemoveNonPrimes(myList):
    """
    RemoveNonPrimes
    """
    print(logic.removeNonPrimes(myList))


def RemovePositives(myList):
    """
    RemovePositives
    """
    print(logic.removePositives(myList))


def UI():  # UI is defined like a menu where you can choose your option for the operation you want to perform on the list
    """
    UI
    """
    go = True  # for the cylce to stop if i enter the option exit
    mainlist = []  # list of lists for undo
    mylist = []  # list with which i work
    i = 0
    mainlist.append(mylist)  # add the empty list
    print(Menu())
    # here is the menu with the options, at some options is necesary to declare helper variables
    while go:

        mylist = mainlist[i][:]  # avoid cache

        option = input("choose option:  ")
        if option == "add new":
            mainlist.append(mylist)
            i += 1
            AddOperation(mylist)

        elif option == "add at last":
            mainlist.append(mylist)
            i += 1
            AddAtLast(mylist)

        elif option == "print list":
            """mainlist.append(mylist)
            i += 1"""
            PrintList(mylist)

        elif option == "remove at index":
            mainlist.append(mylist)
            i += 1
            RemoveAtIndex(mylist)

        elif option == "remove at indexes":
            mainlist.append(mylist)
            i += 1
            RemoveAtIndexes(mylist)

        elif option == "replace":
            mainlist.append(mylist)
            i += 1
            Replace(mylist)

        elif option == "add at index":
            mainlist.append(mylist)
            i += 1
            AddAtIndex(mylist)

        elif option == "replace this with this":
            mainlist.append(mylist)
            i += 1
            ReplaceThisWithThis(mylist)

        elif option == "print prime from to":
            """mainlist.append(mylist)
            i += 1"""
            PrintPrimeFromTo(mylist)

        elif option == "print odd from to":
            """mainlist.append(mylist)
            i += 1"""
            PrintOddFromTo(mylist)

        elif option == "sum from to":
            """mainlist.append(mylist)
            i += 1"""
            SumFromTo(mylist)

        elif option == "gcd from to":
            """mainlist.append(mylist)
            i += 1"""
            GCDFromTo(mylist)

        elif option == "max from to":
            """mainlist.append(mylist)
            i += 1"""
            MAXFromTo(mylist)

        elif option == "remove nonprimes":
            """mainlist.append(mylist)
            i += 1"""
            RemoveNonPrimes(mylist)

        elif option == "remove positives":
            """mainlist.append(mylist)
            i += 1"""
            RemovePositives(mylist)

        elif option == "undo":
            if i <= 0:
                print("no elements in list")
                continue
            i -= 1
            mylist = mainlist[i][:]
            del (mainlist[i + 1])

        elif option == "read from file":
            mainlist.append(logic.ReadFromFile())
            i += 1

        elif option == "write to file":
            logic.WriteToFile(mylist)

        elif option == "exit":
            go = False  # the cycle has to stop

        else:
            print("invalid!!")

        print(mainlist)
        print(Menu())


UI()
