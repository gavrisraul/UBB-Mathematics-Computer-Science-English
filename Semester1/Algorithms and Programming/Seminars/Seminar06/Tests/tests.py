#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""

"""

def test_add():
    repo = StudentRepo()
    s1 = StudentObj(1, "Pop", 10)
    repo.addnew(s1)
    assert repo.size() == 1
    s2 = StudentObj(2, "Ion", 10)
    repo.addnew(s2)
    assert repo.size() == 2
    try:
        repo.addnew(s3)
        assert False
