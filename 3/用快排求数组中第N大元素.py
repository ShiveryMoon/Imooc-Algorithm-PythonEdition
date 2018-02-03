# -*- coding: utf-8 -*-
from random import randint
#此算法的时间复杂度为On

def quickSortFindN(alist,n):
    N = quickSortHelper(alist,0,len(alist)-1,n-1)
    return N

def quickSortHelper(alist,first,last,n):
    splitpoint=partition(alist,first,last)
    if n<splitpoint:
        return quickSortHelper(alist,first,splitpoint-1,n)
    elif n>splitpoint:
        return quickSortHelper(alist,splitpoint+1,last,n)
    else:
        return alist[splitpoint]

def partition(alist,first,last):
    rand = randint(first, last)
    alist[first],alist[rand]=alist[rand],alist[first]
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<pivotvalue:
            leftmark+=1
        while rightmark>=leftmark and alist[rightmark]>pivotvalue:
            rightmark-=1
        if leftmark>rightmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
            leftmark+=1
            rightmark-=1
    alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
N=quickSortFindN(list,11)
print(N)