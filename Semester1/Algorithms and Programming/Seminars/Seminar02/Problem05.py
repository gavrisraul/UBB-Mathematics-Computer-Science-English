#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
5.Determine the k-th element of the sequence 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
5, ....
"""
k = int(input("Give k: "))
i = 1
nr = 1
while nr <= k:
    counter = nr
    while counter > 0:
        i += 1
        if i-1 == k:
            print nr
            break
        counter -= 1
    nr += 1
