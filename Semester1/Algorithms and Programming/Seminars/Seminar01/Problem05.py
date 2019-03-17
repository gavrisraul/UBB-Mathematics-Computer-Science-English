#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
5.Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

myStr = raw_input("Give me the word: ")
for i in range(0, len(myStr)):
    print myStr[: i+1]
