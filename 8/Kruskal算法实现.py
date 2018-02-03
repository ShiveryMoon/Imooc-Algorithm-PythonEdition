# -*- coding: utf-8 -*-
from repo import buildGraphFromFile,SparseGraph,UnionFind
import re
#由于我们没有构造edge类，而Kruskal算法需要用到edge的三个属性：边权重，边的两个节点。所以我们会稍微麻烦一点，需要先把这三个值找到并存起来。

class Kruskal(object):
    def __init__(self,aGraph):
        self.graph=aGraph
        self.edgesList=[] #这里存的是图中所有边的权重和边的两个节点
        self.edgesOfTree=[] #这里存的是，属于最小生成树的那v-1个边的权重和边的两个节点
        self.spanTree()

    def _getEdges(self):
        #我们往edgesList里添加的数据是一个tuple，第一个元素是权重，第二个元素是一个字符串'a-b'，a和b是边两个节点的id。
        vtxList=list(self.graph.vertDict.values())
        while len(vtxList)>1: #如果vtxList里只剩一个vtx，它是不会进入if的判断的，所以是大于1.
            currentVert=vtxList.pop()
            for nextVert in currentVert.getConnections():
                if nextVert in vtxList: #不能往edgesList里添加重复的边
                    self.edgesList.append((currentVert.getWeight(nextVert),'%s-%s' % (nextVert.getId(),currentVert.getId())))

    def spanTree(self):
        self._getEdges()
		self.edgesList.sort()
        uf=UnionFind(self.graph.getVertNum())
        for tuple in self.edgesList:
            if len(self.edgesOfTree) == self.graph.getVertNum():
                break
            v1,v2=[int(i) for i in re.split('\D+',tuple[1])]
            if not uf.isConnected(v1,v2):
                uf.Union(v1,v2)
                self.edgesOfTree.append(tuple)

    def result(self):
        totalWeight=0
        for tuple in self.edgesOfTree:
            totalWeight+=tuple[0]
        return totalWeight

    def edges(self):
        for tuple in self.edgesOfTree:
            print('%s : %s' % (tuple[1],tuple[0]))

g=SparseGraph(weighted=True)
buildGraphFromFile(g,'testG1.txt')
k=Kruskal(g)
k.edges()
print(k.result())



