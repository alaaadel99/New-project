# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def find_nth_occurrence(substr = '', string = '', n= 1):
    index = 0
    index = string.find(substr)
    print('position of first occurrence:', index)
    
    while n >1:
        index = string.find(substr, index+1)
        print('the next positions: ', index)
        n = n -1
        print('n =', n)
    
    return index




##another solution: This code will not run right with overlapping strings
#since it splits the string based on white spaces so it will not detect 
#cases like TestTestTestTest.
def find_nth_occurrence2(substr = '',string = '',n = 1) :
    
    occur = 0
    lst =[]
    index = 0
    count = 0

    # this loop will find the nth occurence
    for i in string.split() :
        if (i == substr) :
            occur += 1
            index = string.find(i, index+count)
            lst.append(index)
            count+=1
            print(f'occurence {occur}')
            print(f'all occurence of "{substr}" till {occur} {lst}')


        #compare the occurence I reached with the required one
        if (occur == n) :
            return f'the {n} occurence of "{substr}" is {lst[-1]}'



    return f'the number of occurence of "{substr}" is less than {n} : {-1}'




def match_string(a,b):
    try:
        s = ''
        for i in b:
            if i not in a:
                s+=i
        #print('difference= ', s)
        if a.count('*') > 1:
            #print('please enter at most one * in a')
            return ('please enter at most one * in a')
        #handle same letters like aa* & aaa
        elif (s =='') and (len(a) <= len(b)) and ("*" in a):
            #print('True')
            return (f'matching? {True}')
        #to avoid not detecting repeated letters like alaa*&alaaadel
        elif (len(a) < len(b)) and ("*" in a) and (a[-1] == "*"):
            index = a.find('*')
            a =a[:index]
            #print('a2 = ',a)
            #print('matching?', a in b)
            return (f'matching? {a in b}')
        #for all other inputs
        else:
            a = a.replace('*',s)
            #print('a= ', a)
            #print('matching?', a==b)
            return (f'matching? {a==b}')
    except TypeError:
        print('an error occured')
    except AttributeError:
        print('an error occured')
    except SyntaxError:
        print('an error occured')




def isPalindrome(text):
    text = str(text) #in case you choose to enter the text not from the user
    l = len(text)
    
    for  i in range  (l// 2 ):
        print(text[i],text[len(text) - 1 - i])
        if text[i] != text[len(text) - 1 - i]:
            return "false, it's not a palindrome"
         
    return "true, it's a Palindrome"





