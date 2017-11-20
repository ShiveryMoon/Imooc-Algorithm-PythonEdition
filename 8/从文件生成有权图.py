# -*- coding: utf-8 -*-
import re
from repo import SparseGraph
#此函数兼容有权图与无权图

def buildGraphFromFile(aGraph,filePath):
    graphList=[]
    hasWeight=False
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f:
            graphList.append([float(x) for x in re.split(r'\s+',line.strip())])
    if len(graphList[0])>2:
        hasWeight=True
    for i in range(len(graphList)):
        if hasWeight:
            aGraph.addEdge(int(graphList[i][0]),int(graphList[i][1]),graphList[i][2])
        else:
            aGraph.addEdge(int(graphList[i][0]),int(graphList[i][1]))

g=SparseGraph(weighted=True)
buildGraphFromFile(g,'testG1.txt')
g.getAllInfo()
