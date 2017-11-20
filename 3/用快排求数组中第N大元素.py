# -*- coding: utf-8 -*-
from random import randint
#此算法的时间复杂度为On

def quickSortFindN(alist,n):
    quickSortHelper(alist,0,len(alist)-1,n-1)
    return alist

def quickSortHelper(alist,first,last,n):
    found=False
    if first<last:
        splitpoint=partition(alist,first,last)
        if n<splitpoint:
            quickSortHelper(alist,first,splitpoint-1,n)
        elif n>splitpoint:
            quickSortHelper(alist,splitpoint+1,last,n)
        else:
            found=True
            print('第%s大的值为: %s' % (n+1,alist[splitpoint]))
            return alist
    if first==last and not found:   #如果first和last重合的情况下第n大的值还没找到，那第n大的值一定就是重合的这个值
        print('第%s大的值为: %s' % (n+1,alist[first]))

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

def insertionSortForQS(alist,first,last):
    for i in range(first+1,last+1):
        currentvalue=alist[i]
        position=i
        while position>first and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
    return alist

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
quickSortFindN(list,8)