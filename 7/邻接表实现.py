# -*- coding: utf-8 -*-
import sys
#由于python的面向对象特性，将定义一个Vertex类，所有与节点有关的属性都储存在vertex类中，比如节点id，节点邻居，节点的前继节点，节点是否被遍历过等等
#注意，此时我们定义的邻接表已经可以存储权重了，也就是说，这个邻接表已经适用于有权无权有向无向图，所以第八章将不会再新实现一个邻接表。

class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} #key是vertex对象，value是两个对象之间的边的权重
        self.ccid = 0 #Connected Components id，即该节点所属的连通分量的id
        self.dist = sys.maxsize
        self.pred = None #当前节点的前继节点
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
        self.vertDict = {} #key是vertex的id，value是vertex
        self.numVertices = 0
        self.directed=directed
        self.weighted=weighted
        self.ccount=0 #一个图有多少个连通分量应当属于图的属性

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