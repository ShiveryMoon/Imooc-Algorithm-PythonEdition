# -*- coding: utf-8 -*-
#size优化就不实现了，太蠢了，我第一次听课的时候以为size优化就是我想象当中的存层数(即rank优化)呢，结果居然存总节点数
#这里的代码直接实装了所有的优化
#话说，并查集真简单。。。

class UnionFind(object):
    def __init__(self,count=10):
        self.count=count
        self.rank=[1 for x in range(count)]
        self.parent=[x for x in range(count)]
        #初始化时所有元素都不互连

    def find(self,p):
        if p>=0 and p<self.count:
            while p != self.parent[p]:
                self.parent[p]=self.parent[self.parent[p]]#这一行代码修改了树结构
                p=self.parent[p]
            return p
            #if p != self.parent[p]:  传说中那更精彩的回答
                #self.parent[p]=self.find(self.parent[p])
            #return parent[p]
        else:
            raise KeyError('Key not in parent')

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)

    def Union(self,p,q):
        pRoot,qRoot=self.find(p),self.find(q)
        if pRoot==qRoot:
            return
        if self.rank[pRoot]<self.rank[qRoot]:
            self.parent[pRoot]=qRoot
        elif self.rank[pRoot]>self.rank[qRoot]:
            self.parent[qRoot]=pRoot
        else:
            self.parent[pRoot]=qRoot
            self.rank[qRoot]+=1

uf=UnionFind(10)
uf.Union(1,2)
uf.Union(1,3)
uf.Union(4,5)
uf.Union(4,6)
uf.Union(3,6)
print(uf.isConnected(0,5))
