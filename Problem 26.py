#!/usr/bin/env python

def FindCycleLenth(n):
    num=1
    remainder=[]
    while num:
        if num<n:
            num*=10
        else:
            break
    while num:
        if num<n:
            num*=10
        num%=n
        if num!=0 and num not in remainder:
            remainder.append(num)
        elif num==0:
            return 0
        else:
            return len(remainder)

def mainfunction():
    maxlen=0
    for n in range(1,1000):
        lentemp=FindCycleLenth(n)
        if lentemp>maxlen:
            maxlen=lentemp
            maxnum=n
    print ('The number is %d, and the cycle lenth is %d' % (maxnum,maxlen))

mainfunction()