#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
logic module for lab 3-5
see pdf for requirements
"""

import math  # for sqrt

# Functions


def add_new(ls, nr):  # add a new element to the list
    """
    Descr: adds a new element to the list
    Input: element
    Output: list
    """
    ls.append(nr)


def add_at_last(ls, nr):  # add a new element to the list at the last position
    """
    Descr: adds a new element at the last position to the list
    Input: element
    Output: list
    """
    ls.insert(len(ls), nr)


# add a new element to the list at the index which is read from the keyboard
def add_at_index(ls, index, nr):
    """
    Descr: adds a new element at a given index
    Input: index, element
    Output: list
    """
    ls.insert(index, nr)


def print_list(ls):  # prints the list
    """
    Descr: prints the list
    Output: list
    """
    print(ls)


# removes an element from the list at the index which is read from the keyboard
def remove_at_index(ls, index):
    """
    Descr: removes an element at index
    Input: index
    Output: list
    """
    del ls[index]


# remove elements from the list between index1 and index2 which are read form the keyboard
def remove_from_to(ls, index1, index2):
    """
    Descr:
    Input: index1, index2
    Output: list
    """
    del ls[index1 : index2 + 1]


def replace(
    ls, nr, index
):  # replaces and element from the list at the index read from the keyboard
    """
    Descr: replaces an element at given index
    Input: element, index
    Output: list
    """
    ls[index] = nr


# help function to replace a sequence with another in the list
def find_first_sublist(seq, sublist, start=0):
    """
    Descr: It helps to find the first appearence of the sublist chosen
    Input: sequence, sublist
    Output: first appearence
    """
    length = len(sublist)
    for index in range(start, len(seq)):
        if seq[index : index + length] == sublist:
            return index, index + length


# function that replace one sequence with another one
def replace_sublist(seq, sublist, replacement):
    """
    Descr: replaces the sublist with a sublist given
    Input: sublist you want to replace
    Output: list
    """
    length = len(replacement)
    index = 0
    for start, end in iter(lambda: find_first_sublist(seq, sublist, index), None):
        seq[start:end] = replacement
        index = start + length


def IsPrime(n):  # check if n is prime or not
    """
    Descr: checks if a number is prime
    Input: number
    Output: True/False
    """
    if n == 0 or n == 1:
        return False
    else:
        for d in range(2, int(math.sqrt(n) + 1)):
            if n % d == 0:
                return False
    return True


def PrimeFromTo(myLst, index1, index2):  # it returns primes from index1 to index2
    """
    Descr: returns primes from index1 to index2
    Input: list, index1, index2
    Output: primes between two indexes
    """
    lst = []
    for i in range(index1, index2 + 1):
        if IsPrime(myLst[i]):
            lst.append(myLst[i])
    return lst


def OddFromTo(myLst, index1, index2):  # it returns odds from index1 to index2
    """
    Descr: returns odds from index1 to index2
    Input: list, index1, index2
    Output: odds between two indexes
    """
    lst = []
    for i in range(index1, index2 + 1):
        if myLst[i] % 2 != 0:
            lst.append(myLst[i])
    return lst


def SumFromTo(myLst, index1, index2):  # sum numbers from index1 to index2
    """
    Descr: Sums elements from index1 to index2
    Input: list, index1, index2
    Output: sum between two indexes
    """
    s = 0
    for i in range(index1, index2 + 1):
        s = s + myLst[i]
    return s


def __gcd(a, b):  # it computes the greatest common divisor between 2 numbers
    """
    Descr: computes the greatest common divisor
    Input: element1, element2
    Output: greatest common divisor
    """
    if a == 0:
        return b
    return __gcd(b % a, a)


# it computes the greatest commom divisor between index1 to index2
def find_gcd(myLst, index1, index2):
    """
    Descr: computes the greatest common divisor of n elements
    Input: list, index1, index2
    Output: greatest common divisor
    """
    gcd = 0
    for i in range(index1, index2 + 1):
        gcd = __gcd(gcd, myLst[i])
    return gcd


def MaxFromTo(myLst, index1, index2):  # it computes the maximum from index1 to index2
    """
    Descr: computes max from index1 to index2
    Input: list, index1, index2
    Output: max
    """
    mx = -9999999
    for i in range(index1, index2 + 1):
        if myLst[i] > mx:
            mx = myLst[i]
    return mx


def removeNonPrimes(myLst):  # it removes nonprimes numbers from the list
    """
    Descr: it removes non primes numbers
    Input: list
    Output: list without non primes
    """
    return [i for i in myLst if IsPrime(i)]


def removePositives(myLst):  # it removes positive numbers from the list
    """
    Descr: it remove positives numbers
    Input: list
    Output: list without positives
    """
    return [i for i in myLst if i < 0]


def Undo(
    lst1, lst2
):  # it makes a simple addition to a variable which is used to undo the operation in the list
    """
    Descr: it undos the last operation
    Input: list
    Output: list at the latest operation
    """
    lst1 = lst2[:]


def ReadFromFile():
    """
    Descr:
    Input:
    Output:
    """
    try:
        fin = open("input.txt", "r")
        mylist = []
        allLines = fin.read()
        lines = allLines.split("\n")
        length = int(lines[0])
        for line in range(1, len(lines) - 1):
            if int(lines[line]):
                mylist.append(int(lines[line]))
            else:
                raise ValueError("Value error")
        l = mylist[:]
        if len(mylist) != length:
            print("You don't have enough numbers in input file!")
        fin.close()
    except IOError as e1:
        print("Something is wrong as IO..." + str(e1))
    except ValueError as e2:
        print("Something is wrong as value..." + str(e2))
    print(l, length)
    return l


def WriteToFile(l):
    """
    Descr:
    Input:
    Output:
    """
    try:
        fout = open("output.txt", "w")
        fout.write(str(l))
        fout.close()
    except IOError as e1:
        print("Something is wrong as IO..." + str(e1))
    except ValueError as e2:
        print("Something is wrong as value..." + str(e2))


# Assert for functions


def test_IsPrime():
    assert IsPrime(0) == False
    assert IsPrime(1) == False
    assert IsPrime(2) == True
    assert IsPrime(3) == True
    assert IsPrime(4) == False


test_IsPrime()


def test___gcd():
    assert __gcd(144, 64) == 16
    assert __gcd(144, 68) == 4
    assert __gcd(10, 5) == 5
    assert __gcd(50, 15) == 5
    assert __gcd(99, 66) == 33


test___gcd()


def test_add_new():
    lst = []
    add_new(lst, 1)
    assert lst == [1]
    add_new(lst, 2)
    assert lst == [1, 2]
    add_new(lst, 3)
    assert lst == [1, 2, 3]
    add_new(lst, 4)
    assert lst == [1, 2, 3, 4]
    add_new(lst, -1)
    assert lst == [1, 2, 3, 4, -1]


test_add_new()


def test_add_at_last():
    lst = []
    add_at_last(lst, 1)
    assert lst == [1]
    add_at_last(lst, 2)
    assert lst == [1, 2]
    add_at_last(lst, 3)
    assert lst == [1, 2, 3]
    add_at_last(lst, 4)
    assert lst == [1, 2, 3, 4]
    add_at_last(lst, -1)
    assert lst == [1, 2, 3, 4, -1]


test_add_at_last()


def test_print_list():  # ????
    lst = [1, 2, 3, 4]
    assert lst == [1, 2, 3, 4]


test_print_list()


def test_add_at_index():
    lst = [1, 2, 3]
    add_at_index(lst, 0, 3)
    assert lst == [3, 1, 2, 3]
    add_at_index(lst, 1, 4)
    assert lst == [3, 4, 1, 2, 3]
    add_at_index(lst, 2, 0)
    assert lst == [3, 4, 0, 1, 2, 3]
    add_at_index(lst, 2, -1)
    assert lst == [3, 4, -1, 0, 1, 2, 3]
    add_at_index(lst, 5, -2)
    assert lst == [3, 4, -1, 0, 1, -2, 2, 3]


test_add_at_index()


def test_remove_at_index():
    lst = [1, 2, 3, 4, 5, 6]
    remove_at_index(lst, 1)
    assert lst == [1, 3, 4, 5, 6]
    remove_at_index(lst, 2)
    assert lst == [1, 3, 5, 6]
    remove_at_index(lst, 3)
    assert lst == [1, 3, 5]
    remove_at_index(lst, 0)
    assert lst == [3, 5]
    remove_at_index(lst, 1)
    assert lst == [3]


test_remove_at_index()


def test_remove_from_to():
    lst = [1, 2, 3, 4, 5, 6]
    remove_from_to(lst, 2, 4)
    assert lst == [1, 2, 6]
    remove_from_to(lst, 0, 1)
    assert lst == [6]


test_remove_from_to()


def test_replace():
    lst = [1, 2, 3, 4, 5]
    replace(lst, 9, 0)
    assert lst == [9, 2, 3, 4, 5]
    replace(lst, -1, 1)
    assert lst == [9, -1, 3, 4, 5]


test_replace()


def test_SumFromTo():
    lst = [1, 2, 3, 4, 5]
    s = SumFromTo(lst, 2, 4)
    assert s == 12
    s = SumFromTo(lst, 0, 2)
    assert s == 6
    s = SumFromTo(lst, 0, 1)
    assert s == 3
    s = SumFromTo(lst, 2, 3)
    assert s == 7
    s = SumFromTo(lst, 3, 4)
    assert s == 9


test_SumFromTo()


def test_find_gcd():
    lst = [144, 68, 256, 2, 1]
    gcd = find_gcd(lst, 0, 2)
    assert gcd == 4
    gcd = find_gcd(lst, 0, 1)
    assert gcd == 4
    gcd = find_gcd(lst, 1, 2)
    assert gcd == 4
    gcd = find_gcd(lst, 3, 4)
    assert gcd == 1
    gcd = find_gcd(lst, 2, 3)
    assert gcd == 2


test_find_gcd()


def test_MaxFromTo():
    lst = [144, 7, 87, 13]
    mx = MaxFromTo(lst, 0, 3)
    assert mx == 144
    mx = MaxFromTo(lst, 1, 3)
    assert mx == 87
    mx = MaxFromTo(lst, 0, 1)
    assert mx == 144
    mx = MaxFromTo(lst, 1, 2)
    assert mx == 87
    mx = MaxFromTo(lst, 2, 3)
    assert mx == 87


test_MaxFromTo()


def test_removeNonPrimes():
    lst = [1, 2, 3, 4, 5]
    assert removeNonPrimes(lst) == [2, 3, 5]


test_removeNonPrimes()


def test_removePositives():
    lst = [-1, 2, -3, 4, -6]
    assert removePositives(lst) == [-1, -3, -6]


test_removePositives()


def test_PrimeFromTo():
    lst = [1, 2, 3, 4, 5]
    assert PrimeFromTo(lst, 0, 4) == [2, 3, 5]
    assert PrimeFromTo(lst, 0, 2) == [2, 3]
    assert PrimeFromTo(lst, 0, 1) == [2]
    assert PrimeFromTo(lst, 3, 4) == [5]
    assert PrimeFromTo(lst, 2, 3) == [3]


test_PrimeFromTo()


def test_OddFromTo():
    lst = [1, 2, 3, 4, 5, 2, 4]
    assert OddFromTo(lst, 0, 3) == [1, 3]
    assert OddFromTo(lst, 3, 5) == [5]
    assert OddFromTo(lst, 0, 1) == [1]
    assert OddFromTo(lst, 1, 2) == [3]
    assert OddFromTo(lst, 3, 4) == [5]


test_OddFromTo()
