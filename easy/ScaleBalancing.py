#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: ScaleBalancing.py
Author: Nigel
Date: 2017/10/13
Description: 
"""


def ScaleBalancing(strArr):

    if len(strArr) != 2: return 'not possible'

    mainArr = [int(x) for x in strArr[0][1:-1].split(",")]
    weightArr = [int(x) for x in strArr[1][1:-1].split(",")]

    _x = int(mainArr[0])
    _y = int(mainArr[1])

    dif = abs(_x - _y)
    if dif in weightArr: return dif
    strArr = 'not possible'
    length = len(weightArr)
    for i in xrange(0, length):
        for j in xrange(0, i):
            if dif == abs(int(weightArr[i]) - int(weightArr[j])) or dif == (int(weightArr[i]) + int(weightArr[j])):
                strArr = "%s,%s" % (weightArr[j], weightArr[i])
                break

    # code goes here
    return strArr


# keep this function call here
if __name__ == "__main__":
    import sys
    print ScaleBalancing(sys.argv[1])