# -*- coding: utf-8 -*-
from repo import SparseGraph,buildGraphFromFile
from pythonds import Queue
#spfa算法就是用队列进行优化的Bellman-Ford算法，老师在9-6提到过。相关资料自行百度。
#spfa算法的时间复杂度是O(KE)，其中K<=2

class Spfa(object):
    def __init__(self,aGraph,start):
        self.graph=aGraph
        self.startVert=aGraph.vertDict[start]
        self.calc()

    def calc(self):
        q=Queue()
        self.startVert.setDistance(0)
        self.startVert.setVisited(True)
        q.enqueue(self.startVert)
        while not q.isEmpty():
            currentVert=q.dequeue()
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    nextVert.setVisited(True)
                    if nextVert not in q:  #这里我对pythonds库的Queue类添加了一个__contains__方法
                        q.enqueue(nextVert)

    def shortestPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        if not self.hasPathTo(w):
            return print('There is no path between %s and %s' % (self.startVert.getId(),w))
        return self.graph.vertDict[w].getDistance()

    def hasPathTo(self,w):
        assert w >= 0 and w < len(self.graph.vertDict)
        return self.graph.vertDict[w].visited()

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
        pathlist = self.shortestPath(w)
        print(pathlist)

g=SparseGraph(directed=True,weighted=True)
buildGraphFromFile(g,'testG2.txt')
S=Spfa(g,0)
print(S.shortestPathTo(4))
S.showPath(4)

'''
对于spfa算法来说，检测是否有负权环的方法是：同一个节点进入队列的次数超过N次(N-1次?)。
这里我偷懒了，没有对图的负权环进行检测，所以不要传入带负权环的图去测试。
'''