#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
see pdf for requirements
"""


def ReadWrite():
    mylist = []
    try:
        fin = open("input.txt", "r")
        fout = open("output.txt", "w")
        allLines = fin.read()
        lines = allLines.split("\n")
        for line in lines:
            mylist.append(line)
        fout.write(str(mylist))
        # print(mylist)
        fin.close()
        fout.close()
    except IOError as e1:
        print("Something is wrong as IO..." + str(e1))
    except ValueError as e2:
        print("Something is wrong as value...", str(e2))


ReadWrite()
