# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile
#这个算法我觉得刘老师解释的不好。。。我是看了别人的博客才搞明白的

class BellmanFord(object):
    def __init__(self,aGraph,start):
        self.graph=aGraph
        self.startVert=aGraph.vertDict[start]
        self.hasNegativeCircle=False
        self.calc()

    def calc(self):
        self.startVert.setDistance(0)
        self.startVert.setVisited(True)
        vertList=list(self.graph.vertDict.values())
        for i in range(len(vertList)-1):
            for currentVert in self.graph:
                for nextVert in currentVert.getConnections():
                    newDist=currentVert.getDistance() + currentVert.getWeight(nextVert)
                    if newDist < nextVert.getDistance():
                        nextVert.setVisited(True) #注：每个节点是可以被多次访问的，我设置visited属性只是为了查询hasPathTo(),不然的话你可以试试把节点3作为起始节点看看会怎么样。
                        nextVert.setDistance(newDist)
                        nextVert.setPred(currentVert)
        self.hasNegativeCircle=self.detectNegativeCircle()

    def detectNegativeCircle(self):
        for currentVert in self.graph:
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    return True

    def negativeCycle(self):
        return self.hasNegativeCircle

    def shortestPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        assert not self.hasNegativeCircle, 'The graph contain negative cycle!'
        if not self.hasPathTo(w):
            return print('There is no path between %s and %s' % (self.startVert.getId(),w))
        return self.graph.vertDict[w].getDistance()

    def hasPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        assert not self.hasNegativeCircle, 'The graph contain negative cycle!'
        return self.graph.vertDict[w].visited()

    def shortestPath(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        assert not self.hasNegativeCircle, 'The graph contain negative cycle!'
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
        assert not self.hasNegativeCircle, 'The graph contain negative cycle!'
        pathlist = self.shortestPath(w)
        print(pathlist)

g=SparseGraph(directed=True,weighted=True)
buildGraphFromFile(g,'testG2.txt')
Bell=BellmanFord(g,0)
print(Bell.shortestPathTo(3))
Bell.showPath(3)
