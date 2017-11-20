# -*- coding: utf-8 -*-
from repo import mergeSort,quickSort
import timeit
from random import randint

#直接使用python的dict对象可以非常容易地实现索引堆。

class IndexMaxHeap(object):
    def __init__(self):
        self.indexList=[0]
        self.items={}
        self.currentSize=0

    def shiftUp(self,i):
        currentvalue=self.items[self.indexList[i]]
        currentindex=self.indexList[i]
        while i//2>0:
            if self.items[self.indexList[i//2]] < currentvalue:
                self.indexList[i]=self.indexList[i//2]
                i=i//2
            else:
                break
        self.indexList[i]=currentindex

    def insert(self,k,value):
        self.indexList.append(k)
        self.items[k]=value
        self.currentSize+=1
        self.shiftUp(self.currentSize)

    def shiftDown(self,i):
        currentvalue=self.items[self.indexList[i]]
        currentindex=self.indexList[i]
        while i*2<=self.currentSize:
            mc=self.maxChild(i)
            if currentvalue < self.items[self.indexList[mc]]:
                self.indexList[i]=self.indexList[mc]
                i=mc
            else:
                break
        self.indexList[i]=currentindex

    def maxChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.items[self.indexList[i*2]]>self.items[self.indexList[i*2+1]]:
                return i*2
            else:
                return i*2+1

    def delFirst(self):
        retval=self.items[self.indexList[1]]
        del self.items[self.indexList[1]]
        if self.currentSize==1:
            self.currentSize-=1
            self.indexList.pop()
            return retval
        self.indexList[1]=self.indexList[self.currentSize]
        self.indexList.pop()
        self.currentSize-=1
        self.shiftDown(1)
        return retval

    def buildHeap(self,items):
        self.items=items
        self.indexList=[0]+list(self.items.keys())
        self.currentSize=items.__len__()
        i=self.currentSize//2
        while i>0:
            self.shiftDown(i)
            i-=1

    def getItem(self,i):
        return self.items[i]

    def maxItemIndex(self):
        return self.indexList[1]

    def change(self,k,newValue):
        if k not in self.indexList:
            raise Exception('%s is not exist!' % k)
        self.items[k]=newValue
        i=self.indexList.index(k)  #index方法的复杂度是O1，根本不需要实现reverse列表。我猜python内部就是靠reverse列表来实现这个index方法的。
        self.shiftDown(i)
        self.shiftUp(i)
        return True


heap=IndexMaxHeap()
items={'John':21,'Lucy':14,'Jesscia':17,'张三':32,'李四':11} #按照分数构成最大堆
heap.buildHeap(items)
heap.insert('Dark',15)
print('最高分: %s %s' % (heap.maxItemIndex(),heap.items[heap.maxItemIndex()]))
print('Lucy多少分? %s' % heap.getItem('Lucy'))
#将Lucy的分数提高到50
heap.change('Lucy',50)
print('最高分: %s %s' % (heap.maxItemIndex(),heap.items[heap.maxItemIndex()]))
heap.delFirst()
print('最高分: %s %s' % (heap.maxItemIndex(),heap.items[heap.maxItemIndex()]))

'''python实现索引堆实在是太舒服了'''