# -*- coding: utf-8 -*-
from random import randint
import timeit
from repo import insertionSort

def mergeSort(alist):
    if len(alist)>1:
        if len(alist)<=16: #优化2
            alist=insertionSort(alist)
            return alist
        mid=len(alist)//2
        lefthalf=alist[:mid]  #切片操作为O(K)，会干扰算法性能
        righthalf=alist[mid:]
        lefthalf=mergeSort(lefthalf)
        righthalf=mergeSort(righthalf)
        if lefthalf[-1] <= righthalf[0]:  #优化1。
            alist=lefthalf+righthalf
            return alist
        i,j,k=0,0,0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<=righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
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
    return alist

def mergeSortBU(alist):
    n=len(alist)
    size=1
    while size<n:
        blist=alist[:]
        i=0
        while i+size<n:
            if alist[i+size-1]<alist[i+size]: #优化1。优化2方案放弃。
                i=i+size+size
                continue
            a,b,c=i,i+size,i
            while a<i+size and b<min(i+size+size,n):
                if blist[a]<=blist[b]:
                    alist[c]=blist[a]
                    a+=1
                else:
                    alist[c]=blist[b]
                    b+=1
                c+=1
            while a<i+size:
                alist[c]=blist[a]
                a+=1
                c+=1
            while b<min(i+size+size,n):
                alist[c]=blist[b]
                b+=1
                c+=1
            i=i+size+size
        size=size+size
    return alist


max=100000
list=[randint(-max,max) for x in range(max)]
alist=list[:]
blist=list[:]
t1=timeit.Timer('mergeSort(alist)','from __main__ import mergeSort,alist')
print('归并排序: %s s' % t1.timeit(number=1))
t2=timeit.Timer('mergeSortBU(blist)','from __main__ import mergeSortBU,blist')
print('BU归并排序: %s s' % t2.timeit(number=1))

'''结论：BU归并算法比普通归并算法平均慢50%，也有可能是因为我的BU归并算法代码还需完善？'''