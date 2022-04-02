# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 19:33:11 2022

@author: Dell
"""

import string_ops

try:
    string = input('please enter the string>> ')
    substr = input('please enter the substring>> ')
    n = int(input('please enter the number of occurence you want>> '))
    print(string_ops.find_nth_occurrence(substr, string, n))
except ValueError:
    print('Number of occurence should be "integer"')


a = input('please enter the first string >> ')
b = input('please enter the second string >> ')
result = string_ops.match_string(a, b)
print(result)


text =input("please enter a text>> ")
print(string_ops.isPalindrome(text))


