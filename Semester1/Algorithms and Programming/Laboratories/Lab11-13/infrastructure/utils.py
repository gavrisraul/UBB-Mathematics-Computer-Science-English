#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
utils functions
"""


def sort_by_function(the_list, the_function):
    for i in range(0, len(the_list)):
        for j in range(i + 1, len(the_list)):
            if the_function(the_list[j], the_list[j + 1]) is False:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]


def filter_by_function(the_list, the_function):
    return list(filter(lambda x: the_function(x), the_list))


def search_by_function(the_list, the_function):
    return [x for x in the_list if the_function(x)]


def combination(the_list, data, start, index, k):
    if index == k:
        yield data[:]

    i = start
    while i <= len(the_list) - 1 and len(the_list) - i >= k - index and index < k:
        data[index] = the_list[i]
        yield from combination(the_list, data, i + 1, index + 1, k)
        i += 1


def get_combinations(the_list, k):
    data = [0] * k
    return [i for i in combination(the_list, data, 0, 0, k)]
