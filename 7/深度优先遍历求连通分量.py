# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile

class ComponentsCounter(object):
    def __init__(self,aGraph):
        self.graph=aGraph
        self.result=0
        self.calc()

    def calc(self):  #result store in both graph.ccount and self.result
        for vertex in self.graph:
            vertex.setVisited(False)
        for vertex in self.graph:
            if not vertex.visited():
                self._dfs(vertex, self.graph.getCcount())
                self.graph.setCcount(self.graph.getCcount()+1)
                self.result+=1

    def _dfs(self, startVertex, ccount):
        startVertex.setCCID(ccount)
        startVertex.setVisited(True)
        for nextVertex in startVertex.getConnections():
            if not nextVertex.visited():
                self._dfs(nextVertex,ccount)

    def getResult(self):
        return self.result

graph=SparseGraph()
buildGraphFromFile(graph,'testG1.txt')
Counter=ComponentsCounter(graph)
print(Counter.getResult())
print(graph.isConnected(0,5))