# -*- coding: utf-8 -*-
from repo import SparseGraph
import sys
from repo import buildGraphFromFile

class PriorityQueue(object):
    #实现一个存储tuple的最小堆来辅助Prim算法。注：这不是一个索引堆，这是一个针对于Prim算法的变种最小二叉堆。
    #不使用索引堆，算法效率确实低了一点，但问题不大，见decreaseKey函数的注释
    def __init__(self):
        self.heapArray=[(0,0)]#tuple[0]用于优先级的比较
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
		#书上此函数的原名是decreaseKey
        #书上说这个函数的时间复杂度是OlogV，那我就来强行分析一波
        #由于不是索引堆，这里要用while遍历来寻找索引i，是个缺点，但问题不大(如果是索引堆的话，找到i的复杂度是O1)。
        #因为虽然while循环看上去是OV，但是第一，这个heapArray是在不断变小的，最后为0。
        #第二，while循环里是不会遍历到后面的maxsize节点的，永远都是遍历到前面一部分就找到vtx的索引了。（除非你瞎传一个vtx进来）
        #所以while循环比OV小，那就是logV好了。
        #剩下那个shiftUp是logV不用说了，所以合起来这个函数的时间复杂度是OlogV。
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

class Prim(object):
    #这里为了方便，我们往vertex对象的dist属性里存储“到前继节点(self.pred)的权值”，而不是字面意义上的distance
    def __init__(self,aGraph,start=0):
        self.graph=aGraph
        self.startVertex=aGraph.vertDict[start]
        self.spanTree()

    def spanTree(self):
        pq=PriorityQueue()
        self.startVertex.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in self.graph]) #tuple[0]是dist，tuple[1]是vertex
        while not pq.isEmpty():
            currentVertex=pq.delMin()
            for nextVertex in currentVertex.getConnections():
                newCost=currentVertex.getWeight(nextVertex)
                if nextVertex in pq and newCost<nextVertex.getDistance():
                    #这两个判断条件，第一个条件（同时也是为了pq.change正常调用）保证了nextVertex是蓝色的点(即不属于已经生成的最小生成树)。
                    #第二个条件保证了每个节点接入树的那条边是权值最小的边。
                    #事实上对于我这个Prim算法的实现方式，这根本算不上优化，这是很正常实现方式。
                    nextVertex.setPred(currentVertex)
                    nextVertex.setDistance(newCost)
                    pq.change(newCost,nextVertex)

    def result(self):
        totalWeight=0
        for vertex in self.graph.vertDict.values():
            totalWeight+=vertex.getDistance()
        return totalWeight

    def edges(self):
        for vertex in list(self.graph.vertDict.values())[1:]: #第一个节点没有pred
            print('%s -> %s : %s' %(vertex.getPred().id,vertex.id,vertex.getDistance()))

g=SparseGraph(weighted=True)
buildGraphFromFile(g,'testG1.txt')
prim=Prim(g)
prim.edges()
print(prim.result())

'''
老师因为创建的是edge类，所以他一开始的优先队列里的数据有E个，优先队列相关操作就是logE
他后来使用了索引堆，就是为了让优先队列里的数据只有V个。
然而我本身就是创建的Vertex类，优先队列里的数据本来也只有V个。
所以，我并不需要把OElogE优化成OElogV，我本来就是OElogV。

还有一点，老师所说的时间复杂度里没有算上buildheap，他直接考虑的就是while循环里的时间复杂度
事实上，buildheap是OV，调用V次delMin是OVlogV。老师在视频里直接把调用delMin(extractMin)的时间复杂度揉进了decreaseKey(insert)里
所以算上buildheap的话，整个Prim算法的时间复杂度是O((V+E)logV)
'''