#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
4.Determine the smallest number that can be formed with the digits of a
number read from keyboard.
Example: for the number 30027 the result is 20037
"""


def nrDig(n):
    """Compute the number of digits of a number"""
    nr = 0
    while n > 0:
        nr += 1
        n = n / 10
    return nr


n = int(input("Give number: "))
v = []
aux = n
min = 9
for i in range(0, nrDig(n)):
    v.append(aux % 10)
    if aux % 10 < min and aux % 10 != 0:
        min = aux % 10
    aux = aux / 10
for i in range(0, nrDig(n)):
    for j in range(i + 1, nrDig(n)):
        if v[i] > v[j]:
            temp = v[i]
            v[i] = v[j]
            v[j] = temp
temp = nrDig(n)
v[0] = min
for i in range(1, temp):
    if v[i] == min:
        v[i] = 0
        break
aux = 0
for i in range(0, temp):
    aux = aux * 10 + v[i]
print(aux)
