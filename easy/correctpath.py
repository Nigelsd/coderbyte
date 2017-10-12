#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: correctpath.py
Author: Nigel
Date: 2017/10/12
Description: coderbyte
"""



def CorrectPath(string):

    x,y=0,0
    str_list=list(string)
    count_r = str_list.count('r')
    count_l = str_list.count('l')
    count_d = str_list.count('d')
    count_u = str_list.count('u')
    value = str_list.count('?')

    current_right_num = abs(count_r - count_l)
    correct_right_num = 4
    current_down_num = abs(count_d - count_u)
    correct_down_num = 4

    for i in xrange(0,len(str_list)):
        if str_list[i] =='r':
            x+=1
        if str_list[i] =='l':
            x+=-1
        if str_list[i] == 'u':
            y+= -1
        if str_list[i] == 'd':
            y+= 1
        if str_list[i] == '?' and correct_right_num > current_right_num and x != 4:
            str_list[i] = 'r'
            value += -1
            current_right_num +=1
            x+=1
        elif str_list[i] == '?' and correct_down_num > current_down_num and y != 4:
            str_list[i] = 'd'
            value += -1
            current_down_num +=1
            y+=1
        elif str_list[i] == '?' and correct_down_num < current_down_num and y !=0:
            str_list[i] = 'u'
            value += -1
            current_down_num += -1
            y+= -1
        elif str_list[i] == '?' and correct_right_num < current_right_num and x!=0:
            str_list[i] ='l'
            value += -1
            current_right_num += -1
            x+= -1
        elif str_list[i] == '?' and correct_right_num == current_right_num and  \
            correct_down_num == current_down_num and x!=4:
            str_list[i] = 'r'
            value += -1
            current_right_num += 1
            x += 1
        elif str_list[i] == '?' and correct_down_num == current_down_num and \
            correct_right_num == current_right_num and y!=0:
            str_list[i] = 'd'
            value += -1
            current_down_num += 1
            y += 1



    res = ''.join(str_list)
    return res

if __name__ == '__main__':
    import sys
    print CorrectPath(sys.argv[1])