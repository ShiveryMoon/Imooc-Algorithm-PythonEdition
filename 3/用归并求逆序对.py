# -*- coding: utf-8 -*-
from repo import mergeSort,quickSort
from random import randint
import timeit

def mergeSortForInversion(alist):
    IN=0
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        LeftIN=mergeSortForInversion(lefthalf)
        RightIN=mergeSortForInversion(righthalf)
        IN=LeftIN+RightIN
        i,j,k=0,0,0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<=righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                IN=IN+len(lefthalf)-i  #真正计算IN的代码，只有这一行
                alist[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            k+=1
            i+=1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            k+=1
            j+=1
    return IN

max=100000
list=[randint(-max,max) for x in range(max)]
print('逆序对的数量: %s' % mergeSortForInversion(list))









