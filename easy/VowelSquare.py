#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: .py
Author: liguanglin(liguanglin@baidu.com)
Date: 2017/
Description: 
"""

def VowelSquare(strArr):
    vowels=['a','e','i','o','u']

    for i in range(0,len(strArr)-1):
        for j in range(0,len(strArr[i])-1):
            if strArr[i][j] in vowels and strArr[i+1][j] in vowels \
                    and strArr[i][j+1] in vowels and strArr[i+1][j+1] in vowels:
                coor="%s-%s"%(i,j)
                return  coor


    return 'not found'

if __name__=="__main__":
    import sys
    VowelSquare(sys.argv[1])

