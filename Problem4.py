#!/usr/bin/env python

def identify(i, j):
    product =i*j
    if len(str(product))%2==0:
        if str(product)[:len(str(product))/2]==str(product)[len(str(product))/2:][::-1]:
            return True
    else:
        return False


def palindromic(n=3):
    # Initialization
    nummax = int('9' * n)
    nummin = int('1' + '0' * (n - 1))
    temp=0
    templist=[]
    for i in range(nummax, nummin - 1, -1):
        for j in range(nummax, nummin - 1, -1):
            a=identify(i,j)
            if a:
                if i*j==temp:
                    temp=i*j
                    templist.append([i,j])
                if i*j>temp:
                    temp=i*j
                    templist=[]
                    templist.append([i,j])
    print('The largest palindromic number for %d-digit numbers :\n'% (n))
    for i in range(len(templist)):
        print('%d * %d = %d\n' % (templist[i][0],templist[i][1],templist[i][0]*templist[i][1]))


if __name__=='__main__':
    palindromic(3)