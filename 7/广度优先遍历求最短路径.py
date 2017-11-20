# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile,Queue

class ShortestPath(object):
    def __init__(self,aGraph,start):
        self.graph=aGraph
        self.startVertex=aGraph.vertDict[start]
        self.calc()

    def calc(self):
        self.startVertex.setDistance(0)
        self.startVertex.setPred(None)
        queue=Queue()
        queue.enqueue(self.startVertex)
        while queue.size()>0:
            currentVertex=queue.dequeue()
            for vertex in currentVertex.getConnections():
                if not vertex.visited():
                    vertex.setDistance(currentVertex.getDistance() + 1)
                    vertex.setVisited(True)
                    vertex.setPred(currentVertex)
                    queue.enqueue(vertex)

    def hasPath(self,w):
        assert w>=0 and w<len(self.graph.vertDict)
        return self.graph.vertDict[w].visited()

    def path(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        if not self.hasPath(w):
            return print('There is no path between %s and %s' % (self.startVertex.getId(),w))
        pathlist=[w]
        currentVertex=self.graph.vertDict[w]
        while currentVertex != self.startVertex:
            currentVertex = currentVertex.getPred()
            pathlist.append(currentVertex.getId())
        pathlist.reverse()
        return pathlist

    def showPath(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        pathlist=self.path(w)
        print(pathlist)

graph=SparseGraph()
buildGraphFromFile(graph,'testG2.txt')
sp=ShortestPath(graph,0)
sp.showPath(3)