# -*- coding: utf-8 -*-
from random import randint
import re
import sys
#由于本人比较懒，把课程需要调用的代码全都堆到这一个文件里了，不太利于阅读，抱歉。。。
#不过，这里的代码是严格按照课程顺序的。
#强烈推荐使用Ctrl+F来查找对应的代码

'''Queue'''#只是因为后面有算法需要使用队列，我才在这里实现了一个队列的。对其他基础数据结构的实现不在此课程范围内。
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __contains__(self, k):
        return k in self.items

'''BubbleSort'''
def bubbleSort(alist):
    exchange=False
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                exchange=True
        if not exchange:
            break
    return alist

'''SelectionSort'''
def selectionSort(alist):
    for i in range(len(alist)):
        minposition=i
        for j in range(i,len(alist)):
            if alist[minposition]>alist[j]:
                minposition=j
        alist[i],alist[minposition]=alist[minposition],alist[i]
    return alist

'''InsertionSort'''
def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue=alist[i]
        position=i
        while alist[position-1]>currentvalue and position>0:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
    return alist

'''ShellSort'''
def shellSort(alist):
    gap=len(alist)//2
    while gap>0:
        for startpos in range(gap):
            gapInsertionSort(alist,startpos,gap)
        gap=gap//2
    return alist

def gapInsertionSort(alist,startpos,gap):
    for i in range(startpos+gap,len(alist),gap):
        position=i
        currentvalue=alist[i]
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue

'''MergeSort'''
def mergeSort(alist):
    if len(alist)>1:
        if len(alist)<=16:
            alist=insertionSort(alist)
            return alist
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        lefthalf=mergeSort(lefthalf)
        righthalf=mergeSort(righthalf)
        if lefthalf[-1] <= righthalf[0]:
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

'''QuickSort2ways'''
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        if last - first <= 16:
            insertionSortForQS(alist, first, last)
        else:
            splitpoint=partition(alist,first,last)
            quickSortHelper(alist,first,splitpoint-1)
            quickSortHelper(alist,splitpoint+1,last)

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

'''QuickSort3Ways'''
def quickSort3Ways(alist):
    quickSort3WaysHelper(alist,0,len(alist)-1)
    return alist

def quickSort3WaysHelper(alist,first,last):
    if first<last:
        if last - first <= 16:
            insertionSortForQS(alist, first, last)
        else:
            ltEnd,gtStart=partition3Ways(alist,first,last)
            quickSort3WaysHelper(alist,first,ltEnd)
            quickSort3WaysHelper(alist,gtStart,last)

def partition3Ways(alist,first,last):
    rand=randint(first,last)
    alist[first], alist[rand] = alist[rand], alist[first]
    pivolvalue=alist[first]
    lt,i,gt=first,first+1,last+1
    done=False
    while not done:
        if alist[i]<pivolvalue:
            alist[lt+1],alist[i]=alist[i],alist[lt+1]
            i+=1
            lt+=1
        elif alist[i]==pivolvalue:
            i+=1
        else:
            alist[gt-1],alist[i]=alist[i],alist[gt-1]
            gt-=1
        if i>=gt:
            done=True
    alist[first],alist[lt]=alist[lt],alist[first]
    lt-=1
    return lt,gt

'''BinHeap'''
class MaxHeap(object):
    def __init__(self,max=100000):
        self.heapList=[0]
        self.currentSize=0
        self.maximum=max

    def shiftUp(self,i):
        currentvalue=self.heapList[i]
        while i//2>0:
            if self.heapList[i//2] < currentvalue:
                self.heapList[i]=self.heapList[i//2]
                i=i//2
            else:
                break
        self.heapList[i]=currentvalue

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.shiftUp(self.currentSize)
        if self.currentSize > self.maximum:
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

    def delFirst(self):
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

class MinHeap(MaxHeap):
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

'''IndexHeap'''
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
        i=self.indexList.index(k)
        self.shiftDown(i)
        self.shiftUp(i)
        return True

'''Priority Queue'''
class PriorityQueue(object):
    def __init__(self):
        self.heapArray=[(0,0)]
        self.currentSize=0

    def buildHeap(self,alist):
        self.heapArray+=alist[:]
        self.currentSize=len(alist)
        i=self.currentSize//2
        while i>0:
            self.shiftDown(i)
            i-=1

    def insert(self,k):
        self.heapArray.append(k)
        self.currentSize+=1
        self.shiftUp(self.currentSize)

    def shiftUp(self,i):
        while i>0:
            if self.heapArray[i][0]<self.heapArray[i//2][0]:
                self.heapArray[i],self.heapArray[i//2]=self.heapArray[i//2],self.heapArray[i]
            i=i//2

    def delMin(self):
        retval=self.heapArray[1][1]
        self.heapArray[1]=self.heapArray[self.currentSize]
        self.heapArray.pop()
        self.currentSize-=1
        self.shiftDown(1)
        return retval

    def shiftDown(self,i):
        while i*2<=self.currentSize:
            mc=self.minChild(i)
            if self.heapArray[i][0]>self.heapArray[mc][0]:
                self.heapArray[i],self.heapArray[mc]=self.heapArray[mc],self.heapArray[i]
            i=i*2

    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapArray[i*2][0]<self.heapArray[i*2+1][0]:
                return i*2
            else:
                return i*2+1

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def __contains__(self, vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False

    def change(self,dist,vtx):
        done=False
        i=1
        while not done and i<=self.currentSize:
            if self.heapArray[i][1]==vtx:
                done=True
            else:
                i+=1
        if done:
            self.heapArray[i]=(dist,vtx)
            self.shiftUp(i)

'''BinarySearch'''
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    while first<=last:
        mid=first+(last-first)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid]<item:
                last=mid-1
            else:
                first=mid+1
    return False

def binarySearchRecursion(alist,item):
    if len(alist)==0:
        return False
    else:
        mid=len(alist)//2
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            return binarySearchRecursion(alist[mid+1:],item)
        else:
            return binarySearchRecursion(alist[:mid],item)

'''BinarySearchTree'''
class TreeNode(object):
    def __init__(self,key,value,parent=None,left=None,right=None):
        self.key=key
        self.value=value
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
        self.nodeCount=1
        self.balanceFactor = 0
        self.isleftchild = False
        self.isrightchild = False

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def addChildAttr(self):
        if self.isLeftChild():
            self.isleftchild=True
        else:
            self.isrightchild=True

    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.value=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        current = self.rightChild
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findPredecessor(self):
        current = self.leftChild
        while current.hasRightChild():
            current = current.rightChild
        return current

class BinarySearchTree(object):
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,value):
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root=TreeNode(key,value)
        self.size=self.size + 1

    def _put(self,key,value,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,value,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,value,parent=currentNode)
        elif key==currentNode.key:
            currentNode.value=value
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,value,parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if currentNode is None:
            return None
        elif currentNode.key==key:
            return currentNode
        elif currentNode.key>key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item,self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value

        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def preOrder(self):
        self._preOrder(self.root)

    def _preOrder(self,treeNode):
        if treeNode:
            print(treeNode.key)
            self._preOrder(treeNode.leftChild)
            self._preOrder(treeNode.rightChild)

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self,treeNode):
        if treeNode:
            self._inOrder(treeNode.leftChild)
            print(treeNode.key)
            self._inOrder(treeNode.rightChild)

    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self,treeNode):
        if treeNode:
            self._postOrder(treeNode.leftChild)
            self._postOrder(treeNode.rightChild)
            print(treeNode.key)

    def levelOrder(self):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            treeNode = q.dequeue()
            print(treeNode.key)
            if treeNode.leftChild:
                q.enqueue(treeNode.leftChild)
            if treeNode.rightChild:
                q.enqueue(treeNode.rightChild)

    def minimum(self):
        node = self.root
        while node.leftChild:
            node = node.leftChild
        return node.key

    def maximum(self):
        node=self.root
        while node.rightChild:
            node=node.rightChild
        return node.key

    def getFloorAndCeil(self,key):
        return self._getFloorAndCeil(self.root,key,None,None)

    def _getFloorAndCeil(self,currentNode,key,floor,ceil):
        if currentNode:
            if currentNode.key==key:
                floor,ceil=key,key
                return floor,ceil
            else:
                if currentNode.key<key:
                    floor=currentNode.key
                    return self._getFloorAndCeil(currentNode.rightChild,key,floor,ceil)
                else:
                    ceil=currentNode.key
                    return self._getFloorAndCeil(currentNode.leftChild,key,floor,ceil)
        else:
            return floor,ceil

'''AVLTree'''
class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild, insert=True)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild, insert=True)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                if nodeToRemove.hasBothChildren():
                    succ=nodeToRemove.findSuccessor()
                    succ.addChildAttr()
                    self.remove(nodeToRemove)
                    nodeToRemove=succ
                else:
                    nodeToRemove.addChildAttr()
                    self.remove(nodeToRemove)
                self.updateBalance(nodeToRemove,first2delete=True)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def updateBalance(self, node, insert=False, delete=False, first2delete=False):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if insert:
                if node.isLeftChild():
                    node.parent.balanceFactor += 1
                elif node.isRightChild():
                    node.parent.balanceFactor -= 1
                if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent, insert=True)
            if first2delete:
                recursion=False
                if node.parent.balanceFactor != 0:
                    recursion=True
                if node.isleftchild:
                    node.parent.balanceFactor -= 1
                elif node.isrightchild:
                    node.parent.balanceFactor += 1
                if recursion:
                    self.updateBalance(node.parent, delete=True)
            if delete:
                recursion = False
                if node.parent.balanceFactor != 0:
                    recursion = True
                if node.isLeftChild():
                    node.parent.balanceFactor -= 1
                elif node.isRightChild():
                    node.parent.balanceFactor += 1
                if recursion:
                    self.updateBalance(node.parent, delete=True)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor -1 - max(newRoot.balanceFactor,0)
        newRoot.balanceFactor=newRoot.balanceFactor -1 + min(rotRoot.balanceFactor,0)

'''UnionFind'''
class UnionFind(object):
    def __init__(self,count):
        self.count=count
        self.rank=[1 for x in range(count)]
        self.parent=[x for x in range(count)]

    def find(self,p):
        if p>=0 and p<self.count:
            while p != self.parent[p]:
                self.parent[p]=self.parent[self.parent[p]]
                p=self.parent[p]
            return p
        else:
            raise KeyError('Key not in parent')

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)

    def Union(self,p,q):
        pRoot,qRoot=self.find(p),self.find(q)
        if pRoot==qRoot:
            return
        if self.rank[pRoot]<self.rank[qRoot]:
            self.parent[pRoot]=qRoot
        elif self.rank[pRoot]>self.rank[qRoot]:
            self.parent[qRoot]=pRoot
        else:
            self.parent[pRoot]=qRoot
            self.rank[qRoot]+=1

'''Adjacency Matrix'''
class DenseGraph(object):
    def __init__(self,n,directed=False):
        self.n=n
        self.m=0
        self.directed=directed
        self.martix=[[0 for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.martix:
            print(str(line))
        return ''

    def getNumberOfVertex(self):
        return self.n

    def getNumberOfEdge(self):
        return self.m

    def addEdge(self, v, w):
        if 0<=v<self.n and 0<=w<self.n:
            if self.hasEdge(v,w):
                return
            self.martix[v][w]=1
            if self.directed is False:
                self.martix[w][v]=1
            self.m+=1
        else:
            raise Exception('Vertex not in the graph')

    def hasEdge(self,v,w):
        if 0<=v<self.n and 0<=w<self.n:
            return self.martix[v][w]
        else:
            raise Exception('Vertex not in the graph')

'''Adjacency List'''
class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.ccid = 0
        self.dist = sys.maxsize
        self.pred = None
        self.isvisited = False

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getConnectionsId(self):
        idList=[]
        for k in self.connectedTo.keys():
            idList.append(k.getId())
        return sorted(idList)

    def getConnectionsIdAndWeight(self):
        idList = []
        for k in self.connectedTo.keys():
            idList.append(k.getId())
        weightList=list(self.connectedTo.values())
        return {idList[i]:weightList[i] for i in range(len(idList))}

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id

    def getCCID(self):
        return self.ccid

    def setCCID(self,ccid):
        self.ccid=ccid

    def getPred(self):
        return self.pred

    def setPred(self,pred):
        self.pred=pred

    def visited(self):
        return self.isvisited

    def setVisited(self,bool):
        self.isvisited=bool

    def getDistance(self):
        return self.dist

    def setDistance(self, dist):
        self.dist = dist

class SparseGraph(object):
    def __init__(self,directed=False,weighted=False):
        self.vertDict = {}
        self.numVertices = 0
        self.directed=directed
        self.weighted=weighted
        self.ccount=0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertDict[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertDict

    def addEdge(self,f,t,weight=0):
        if f not in self.vertDict:
            self.addVertex(f)
        if t not in self.vertDict:
            self.addVertex(t)
        self.vertDict[f].addNeighbor(self.vertDict[t], weight)
        if self.directed is False:
            self.vertDict[t].addNeighbor(self.vertDict[f], weight)

    def getVertices(self):
        return list(self.vertDict.keys())

    def getVertNum(self):
        return self.numVertices

    def __iter__(self):
        return iter(self.vertDict.values())

    def getAllInfo(self):
        verticesList=[int(x) for x in list(self.getVertices())]
        verticesList.sort()
        if self.weighted:
            for i in range(len(verticesList)):
                print('vertex %s : %s' % (i, self.getVertex(i).getConnectionsIdAndWeight()))
        else:
            for i in range(len(verticesList)):
                print('vertex %s : %s' %(i,self.getVertex(i).getConnectionsId()))

    def isConnected(self,p,q):
        return self.vertDict[p].getCCID() == self.vertDict[q].getCCID()

    def getCcount(self):
        return self.ccount

    def setCcount(self,ccount):
        self.ccount=ccount

'''buildGraphFromFile'''
def buildGraphFromFile(aGraph,filePath):
    graphList=[]
    hasWeight=False
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f:
            graphList.append([float(x) for x in re.split(r'\s+',line.strip())])
    if len(graphList[0])>2:
        hasWeight=True
    for i in range(len(graphList)):
        if hasWeight:
            aGraph.addEdge(int(graphList[i][0]),int(graphList[i][1]),graphList[i][2])
        else:
            aGraph.addEdge(int(graphList[i][0]),int(graphList[i][1]))