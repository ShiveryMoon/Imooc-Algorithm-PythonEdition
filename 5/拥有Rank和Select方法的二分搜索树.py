# -*- coding: utf-8 -*-
from repo import TreeNode,BinarySearchTree
#这里我们做一个BST的继承类来实现rank和select方法。因为，如下面你将看到的，这两个方法使得BST的添加和删除操作变成O(logn)²，所以我认为不能直接实现在原来的类中。
#这是我自己想到的实现方法，并没有借鉴老师在github上的代码，也许老师的方案更好。

class EXBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super(EXBinarySearchTree, self).__init__()

    def updateNodeCount(self,treeNode,insert=False,remove=False):
        '''
        我们通过这个函数来给每个节点设置合适的nodeCount。
        仔细思考一下，当我们插入或删除一个节点的时候，只有该节点的所有祖宗的nodeCount会变
        所以，顺着该节点一路往上修改父节点的nodeCount即可

        我们来分析一下这个函数的时间复杂度。由于在每一层我们只进行一次操作，所以时间复杂度为Ologn
        所以，当我们在put函数和delete函数中调用了这个函数以后，put和delete的时间复杂度变为O(logn)²
        '''

        if insert:
            while treeNode is not self.root:
                treeNode=treeNode.parent
                treeNode.nodeCount+=1
        if remove:
            while treeNode is not self.root:
                treeNode=treeNode.parent
                treeNode.nodeCount-=1

    def put(self,key,value):
        if self.root:
            currentNode=self._put(key,value,self.root)
            self.updateNodeCount(currentNode,insert=True)
        else:
            self.root=TreeNode(key,value)
        self.size=self.size + 1

    def _put(self,key,value,currentNode):  #这里，我们修改该函数的目的是让该函数能够返回插入的节点，之前的_put是没有return的
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                return self._put(key,value,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,value,parent=currentNode)
                return currentNode.leftChild
        elif key==currentNode.key:
            currentNode.value=value
            return currentNode
        else:
            if currentNode.hasRightChild():
                return self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,value,parent=currentNode)
                return currentNode.rightChild

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                if nodeToRemove.hasBothChildren():
                    succ=nodeToRemove.findSuccessor() #这里要注意，当我们要使用Hubbard Deletion时，实际上我们删除的是后继节点，所以我们要将后继节点传入updateNodeCount
                    self.remove(nodeToRemove)
                    nodeToRemove=succ
                else:
                    self.remove(nodeToRemove)
                self.updateNodeCount(nodeToRemove,remove=True)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def getNodeCount(self,key):
        node=self._get(key,self.root)
        return node.nodeCount

    def rank(self,key):
        if key not in self:
            raise KeyError('Error, key not in tree')
        node=self._get(key,self.root)
        if node.isRoot():
            if node.hasLeftChild():
                return node.leftChild.nodeCount + 1
            else:
                return 1
        else:
            if node.isLeftChild():
                rightcount=0
                if node.hasRightChild():
                    rightcount=node.rightChild.nodeCount
                return self.rank(node.parent.key) - 1 - rightcount
            else:
                leftcount=0
                if node.hasLeftChild():
                    leftcount=node.leftChild.nodeCount
                return self.rank(node.parent.key) + 1 +leftcount

    def select(self,rank):
        if rank>self.size:
            raise Exception('Error, rank out of size')
        return self._select(rank,self.root)

    def _select(self,rank,treeNode):
        if self.rank(treeNode.key)==rank:
            return treeNode.key
        elif self.rank(treeNode.key)<rank:
            return self._select(rank,treeNode.rightChild)
        else:
            return self._select(rank,treeNode.leftChild)


tree=EXBinarySearchTree()
tree[28]='a'
tree[16]='b'
tree[30]='c'
tree[13]='d'
tree[22]='e'
tree[29]='f'
tree[42]='g'
