# -*- coding: utf-8 -*-
from pythonds import Queue
#支持重复元素的二分搜索树就不实现了，因为这违背了字典的定义，同一个key下不能存储多个value

class TreeNode(object):
    def __init__(self,key,value,parent=None,left=None,right=None):
        self.key=key
        self.value=value
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
        self.nodeCount=1 #此属性用于rank和select
        self.balanceFactor=0 #此属性用于AVL树
        self.isleftchild=False #此属性仅用于AVL树中删除节点时的平衡因子更新
        self.isrightchild=False #此属性仅用于AVL树中删除节点时的平衡因子更新

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def addChildAttr(self): #此函数仅在AVL树删除节点时调用，来辅助平衡因子更新
        if self.isLeftChild():
            self.isleftchild=True
        else:
            self.isrightchild=True

    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.value=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self

    def spliceOut(self):
        #这个函数的效果是删除自身这个节点，用于辅助Hubbard Deletion。其实这就是下面的remove函数里的两种简单情况(leaf or has one child)，代码几乎相同。
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        current = self.rightChild
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findPredecessor(self):
        current = self.leftChild
        while current.hasRightChild():
            current = current.rightChild
        return current

class BinarySearchTree(object):
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,value):  #即insert
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root=TreeNode(key,value)
        self.size=self.size + 1

    def _put(self,key,value,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,value,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,value,parent=currentNode)
        elif key==currentNode.key:
            currentNode.value=value
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,value,parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key):  #即search
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if currentNode is None:
            return None
        elif currentNode.key==key:
            return currentNode
        elif currentNode.key>key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item,self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode): #delete函数的辅助函数
        if currentNode.isLeaf():  # this node is leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #Hubbard Deletion
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def preOrder(self):
        self._preOrder(self.root)

    def _preOrder(self,treeNode):
        if treeNode:
            print(treeNode.key)
            self._preOrder(treeNode.leftChild)
            self._preOrder(treeNode.rightChild)

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self,treeNode):
        if treeNode:
            self._inOrder(treeNode.leftChild)
            print(treeNode.key)
            self._inOrder(treeNode.rightChild)

    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self,treeNode):
        if treeNode:
            self._postOrder(treeNode.leftChild)
            self._postOrder(treeNode.rightChild)
            print(treeNode.key)

    def levelOrder(self):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            treeNode = q.dequeue()
            print(treeNode.key)
            if treeNode.leftChild:
                q.enqueue(treeNode.leftChild)
            if treeNode.rightChild:
                q.enqueue(treeNode.rightChild)

    def minimum(self): #return the smallest key of the tree
        node = self.root
        while node.leftChild:
            node = node.leftChild
        return node.key

    def maximum(self): # return the largest key of the tree
        node=self.root
        while node.rightChild:
            node=node.rightChild
        return node.key

    def getFloorAndCeil(self,key):
        return self._getFloorAndCeil(self.root,key,None,None)

    def _getFloorAndCeil(self,currentNode,key,floor,ceil):
        if currentNode:
            if currentNode.key==key:
                floor,ceil=key,key
                return floor,ceil
            else:
                if currentNode.key<key:
                    floor=currentNode.key
                    return self._getFloorAndCeil(currentNode.rightChild,key,floor,ceil)
                else:
                    ceil=currentNode.key
                    return self._getFloorAndCeil(currentNode.leftChild,key,floor,ceil)
        else:
            return floor,ceil

tree=BinarySearchTree()
tree[28]='a'
tree[16]='b'
tree[30]='c'
tree[13]='d'
tree[22]='e'
tree[29]='f'
tree[42]='g'