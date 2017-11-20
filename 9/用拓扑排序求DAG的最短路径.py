# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile

class TopologicalSort(object):
    def __init__(self,aGraph):
        self.graph=aGraph
        self.vertList=[]
        self.isSorted=False
        self.TpSort()

    def TpSort(self):
        for vert in self.graph:
            vert.setVisited(False)
        for vert in self.graph:
            if not vert.visited():
                self._dps(vert)
        self.isSorted=True
        self.vertList.reverse()

    def _dps(self,startVert):
        startVert.setVisited(True)
        for nextVert in startVert.getConnections():
            if not nextVert.visited():
                self._dps(nextVert)
        self.vertList.append(startVert) #理解这段代码是理解拓扑排序的关键

    def showListById(self):
        if self.isSorted:
            return [vert.getId() for vert in self.vertList]

    def getSortedList(self):
        if self.isSorted:
            return self.vertList

class DAGShortestPath(object):
    def __init__(self,TPList,start):
        self.tplist=TPList
        self.start=start
        self.startVert=None
        self.vertDict={}
        self.calc()

    def _init(self): #为了使构造函数更简洁，该类使用更方便，我并不传入graph对象，但这样就需要我自己构造vertDict
        for vert in self.tplist:
            self.vertDict[vert.getId()]=vert
        for vert in self.tplist:
            vert.setVisited(False)

    def calc(self):
        self._init()
        self.startVert=self.vertDict[self.start]
        self.startVert.setDistance(0)
        self.startVert.setVisited(True)
        for currentVert in self.tplist:
            for nextVert in currentVert.getConnections():
                newDist=currentVert.getDistance()+currentVert.getWeight(nextVert)
                if newDist<nextVert.getDistance():
                    nextVert.setVisited(True) #注：每个节点是可以被多次访问的，我设置visited属性只是为了查询hasPathTo()
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newDist)

    def hasPathTo(self,w):
        assert w >= 0 and w < len(self.vertDict)
        return self.vertDict[w].visited()

    def shortestPathTo(self,w):
        assert w >= 0 and w < len(self.vertDict)
        assert self.hasPathTo(w), 'There is no path!'
        return self.vertDict[w].getDistance()

    def shortestPath(self,w):
        assert w >= 0 and w < len(self.vertDict)
        assert self.hasPathTo(w), 'There is no path!'
        pathlist = [w]
        currentVert = self.vertDict[w]
        while currentVert != self.startVert:
            currentVert = currentVert.getPred()
            pathlist.append(currentVert.getId())
        pathlist.reverse()
        return pathlist

    def showPath(self,w):
        assert w >= 0 and w < len(self.vertDict)
        assert self.hasPathTo(w), 'There is no path!'
        pathlist=self.shortestPath(w)
        print(pathlist)

g=SparseGraph(directed=True,weighted=True)
buildGraphFromFile(g,'testDAG.txt')
T=TopologicalSort(g)
DAG=DAGShortestPath(T.getSortedList(),2)
print(DAG.shortestPathTo(6))
DAG.showPath(6)

'''
这个实现是这样的：
先定义一个类求出DAG的拓扑排序，装在一个list中。
然后再定义一个求DAG最短路径的类，这个类接受一个装载拓扑排序结果的list和源id
这两个类之间没关系，每个类都可以拿出来单独调用。

其实也可以把这两个类的操作合并成一个类，但我懒得考虑如何实现更合理了，反正算法思想已经实现出来了
'''