#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
3.Verify if a given number is perfect square.
"""

import math


def PerfSquare1(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    else:
        return 0


def PerfSquare2(n):
    ok = 0
    for i in range(1, n):
        aux = i * i
        if aux == n:
            ok = 1
            break
    return ok


n = int(input("Give number: "))
if PerfSquare1(n) == 1:
    print("Number is PS")
else:
    print("Number isn't PS")
n = int(input("Give number: "))
if PerfSquare2(n) == 1:
    print("Number is PS")
else:
    print("Number isn't PS")

