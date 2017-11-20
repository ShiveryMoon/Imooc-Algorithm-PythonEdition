# -*- coding: utf-8 -*-
from repo import PriorityQueue,SparseGraph,buildGraphFromFile

class Dijkstra(object):
    def __init__(self,aGraph,start):
        self.graph=aGraph
        self.startVert=aGraph.vertDict[start]
        self.calc()

    def calc(self):
        #这里我做了一个小改动，使得Dij算法能够操作非连通图，而书上原本的算法是无法操作非连通图的。
        #原理其实和广度优先遍历求最短路径一样，那就是，不要调用pq.buildHeap把所有节点全都放进优先队列(Prim就是这么干的，因为Prim只能操作连通图)
        #我们一个个将节点insert进优先队列就行，这样，另一个连通分量的节点永远不会进入优先队列。
        pq=PriorityQueue()
        self.startVert.setDistance(0)
        self.startVert.setPred(None)
        self.startVert.setVisited(True)
        pq.insert((self.startVert.getDistance(),self.startVert))
        while not pq.isEmpty():
            currentVert=pq.delMin()
            for nextVert in currentVert.getConnections():
                newDist=currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist<nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newDist)
                    nextVert.setVisited(True)
                    if nextVert in pq:
                        pq.change(newDist,nextVert)
                    else:
                        pq.insert((newDist,nextVert))

    def hasPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        return self.graph.vertDict[w].visited()

    def shortestPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        return self.graph.vertDict[w].getDistance()

    def shortestPath(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        if not self.hasPathTo(w):
            return print('There is no path between %s and %s' % (self.startVert.getId(),w))
        pathlist=[w]
        currentVert=self.graph.vertDict[w]
        while currentVert != self.startVert:
            currentVert=currentVert.getPred()
            pathlist.append(currentVert.getId())
        pathlist.reverse()
        return pathlist

    def showPath(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        pathlist=self.shortestPath(w)
        print(pathlist)

g=SparseGraph(directed=True,weighted=True)
buildGraphFromFile(g,'testG1.txt')
Dij=Dijkstra(g,0)
print('Shortest Path To 4 : %s' % Dij.shortestPathTo(4))
Dij.showPath(4)

