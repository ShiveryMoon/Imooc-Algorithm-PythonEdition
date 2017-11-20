# -*- coding: utf-8 -*-
from repo import mergeSort,quickSort
import timeit
from random import randint
#这里我实施了课程中的heap sort2和heap sort3，分别对应了HeapSort和HeapSortInPlace。第一个算法太简单、算法效率低，直接忽略。
#定义类的时候的参数max，出现在课程4-10中，它限制了堆中元素的个数，可用于以Onlogm的复杂度求n个元素里优先级最大的m个元素。

class MaxHeap(object):
    def __init__(self,max=100000):
        self.heapList=[0]
        self.currentSize=0
        self.maximum=max

    def shiftUp(self,i):
        currentvalue=self.heapList[i]
        while i//2>0:
            if self.heapList[i//2] < currentvalue:
                self.heapList[i]=self.heapList[i//2]   #优化：赋值替代交换
                i=i//2
            else:
                break
        self.heapList[i]=currentvalue

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.shiftUp(self.currentSize)
        if self.currentSize>self.maximum:  #在最大堆中这个操作会保留m个最小的元素。
            self.delFirst()

    def shiftDown(self,i):
        currentvalue=self.heapList[i]
        while i*2<=self.currentSize:
            mc=self.maxChild(i)
            if currentvalue < self.heapList[mc]:
                self.heapList[i]=self.heapList[mc]
                i=mc
            else:
                break
        self.heapList[i]=currentvalue

    def maxChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]>self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delFirst(self):  #之所以叫delFirst是因为这个函数可以兼容最大堆和最小堆
        retval=self.heapList[1]
        if self.currentSize==1:
            self.currentSize-=1
            self.heapList.pop()
            return retval
        self.heapList[1]=self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize-=1
        self.shiftDown(1)
        return retval

    def buildHeap(self,alist): #heapify
        self.heapList=[0]+alist[:]
        self.currentSize=len(alist)
        i=self.currentSize//2
        while i>0:
            self.shiftDown(i)
            i-=1
        overflow=self.currentSize-self.maximum
        for i in range(overflow):
            self.delFirst()

    def HeapSort(self,alist):
        self.buildHeap(alist)
        return [self.delFirst() for x in range(self.currentSize)]

    def HeapSortInPlace(self,alist):
        self.buildHeap(alist)
        while self.currentSize>1:
            self.heapList[1],self.heapList[self.currentSize]=self.heapList[self.currentSize],self.heapList[1]
            self.currentSize-=1
            self.shiftDown(1)
        return self.heapList

class MinHeap(MaxHeap): #最小堆，继承自MaxHeap，覆盖了父类的上浮和下沉操作，酌情使用。
    def __init__(self):
        super(MaxHeap, self).__init__()

    def shiftUp(self,i):
        currentvalue=self.heapList[i]
        while i//2 > 0:
            if self.heapList[i//2] > currentvalue:
                self.heapList[i]=self.heapList[i//2]
                i//2
            else:
                break
        self.heapList[i] = currentvalue

    def shiftDown(self,i):
        currentvalue=self.heapList[i]
        while i*2<=self.currentSize:
            mc=self.minChild(i)
            if currentvalue > self.heapList[mc]:
                self.heapList[i]=self.heapList[mc]
                i=mc
            else:
                break
        self.heapList[i]=currentvalue

    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] <self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

heap=MaxHeap()
max=50000
list=[randint(-max,max) for x in range(max)]
alist=list[:]
blist=list[:]
clist=list[:]
t1=timeit.Timer('heap.HeapSort(alist)','from __main__ import heap,alist')
print('堆排序: %s s' % t1.timeit(number=1))
t2=timeit.Timer('heap.HeapSortInPlace(blist)','from __main__ import heap,blist')
print('堆原地排序: %s s' % t2.timeit(number=1))
t3=timeit.Timer('quickSort(clist)','from __main__ import quickSort,clist')
print('快速排序: %s s' % t3.timeit(number=1))


