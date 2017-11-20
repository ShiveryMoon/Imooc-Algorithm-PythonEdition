# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile

class SearchPath(object):
    def __init__(self,aGraph,startKey):
        self.graph=aGraph
        self.startVertex=aGraph.vertDict[startKey]
        self.pathlist=[]
        self.calc()

    def calc(self):
        for vertex in self.graph:
            vertex.setVisited(False)
            vertex.setPred(None)
        self._dfs(self.startVertex)

    def _dfs(self,startVertex):
        for nextVertex in startVertex.getConnections():
            if not nextVertex.visited():
                nextVertex.setVisited(True)
                nextVertex.setPred(startVertex)
                self._dfs(nextVertex)

    def hasPath(self,w):
        return self.graph.vertDict[w].visited()

    def path(self,w):  #老师三个函数里没有将具体路径返回的函数，我认为是有必要的，所以我让path函数返回了pathlist
        if not self.hasPath(w):
            return print('There is no path between %s and %s' % (self.startVertex.getId(),w))
        self.pathlist=[w]
        currentVertex=self.graph.vertDict[w]
        while currentVertex != self.startVertex:
            currentVertex = currentVertex.getPred()
            self.pathlist.append(currentVertex.getId())
        self.pathlist.reverse()
        return self.pathlist

    def showPath(self,w):
        self.pathlist=[]
        self.path(w)
        if self.pathlist:
            print(self.pathlist)

graph=SparseGraph(directed=True)
buildGraphFromFile(graph,'testG2.txt')
path=SearchPath(graph,3)
path.showPath(5)
path.showPath(4)
