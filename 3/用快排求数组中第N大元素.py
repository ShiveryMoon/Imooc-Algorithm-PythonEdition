# -*- coding: utf-8 -*-
from random import randint
#此算法的时间复杂度为On

def quickSortFindN(alist,n):
    N = quickSortHelper(alist,0,len(alist)-1,len(alist)-n)
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

list=[2,1]
N=quickSortFindN(list,1)
print(N)