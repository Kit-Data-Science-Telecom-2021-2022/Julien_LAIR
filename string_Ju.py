# string1
# !/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: ', where is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    if isinstance(count, int):
        if count < 10 : 
            return 'Number of donuts: {}'.format(count)
        else:
            return 'Number of donuts: many'
    else: return ""

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(s):
    l = list(s)
    if len(l) >= 2:
        return l[0]+l[1]+l[-2]+l[-1]
    else:
        return ""

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to "*", except do not change
# the first char itself.
# e.g. "babble" yields "ba**le"
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(s):
    l = list(s)
    if len(l)>1:
        h0 = l[0]
        h1 = l[1:len(l)]
        h1 = "".join(h1)
        h1 = h1.replace(l[0], "*")
        h = h0+h1
        return h
    elif len(l)==1: return "*"
    else: return ""

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space 'a b', except swap the first 2 chars of each string.
# e.g.
# 'mix', 'pod' -> 'pox mid'
# 'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

def mix_up(a, b):
    l=list(a)
    h=list(b)
    if len(l)>=2 and len(h)>=2:
        l0 = l[0]+l[1]
        l1 = l[2:len(l)]
        h0 = h[0]+h[1]
        h1 = h[2:len(h)]
        l = h0 + "".join(l1)
        h = l0 + "".join(h1)
        s = l+" "+h
        return s
    else: return ""

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.

def main():
    print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print ('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print
    print ('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print ('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

# Standard boilerplate to call the main() function.

if __name__ == '__main__':
    main()

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    l = list(s)
    if len(l)>=3:
        l0 = l[-3]+l[-2]+l[-1]
        l0 = "".join(l0)
        if l0 == "ing":
            s = s+"ly"
            return s
        else:
            s = s+"ing"
            return s
    else: return s 

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    l = list(s)
    f = len(l) - 2
    n=0
    m=0
    
    for i in range(f):
        if l[i]+l[i+1]+l[i+2] == "not":n=i
            
    for i in range(f):
        if l[i]+l[i+1]+l[i+2] == "bad":m=i+2
    
    if m<n:
        return s
    
    else:
        p = "".join(l[n:m+1])
        s = s.replace(p, "good")
        return s
    
# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
# a-front + b-front + a-back + b-back

def front_back(a, b):
    l1 = list(a)
    l2 = list(b)
    
    if len(l1)%2 == 0:
        c0 = len(l1)//2
        c1 = len(l1) + 1
        l11 = a[:c0]
        l12 = a[c0:c1]
    else:
        c0 = (len(l1)//2) + 1
        c1 = len(l1) + 1
        l11 = a[:c0]
        l12 = a[c0:c1]

    
    if len(l2)%2 == 0:
        c0 = len(l2)//2
        c1 = len(l2) + 1
        l21 = b[:c0]
        l22 = b[c0:c1]
    else:
        c0 = (len(l2)//2) + 1
        c1 = len(l2) + 1
        l21 = b[:c0]
        l22 = b[c0:c1]
        
    s = l11 + l21 + l12 + l22
    return s

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.

def main():
    print ('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print ('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print ('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()