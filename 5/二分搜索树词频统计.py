# -*- coding: utf-8 -*-
import re
from repo import BinarySearchTree
#词频统计出现在课程5-4的最后，老师想检测二分搜索树的查找效率并与顺序数组作比较。这里我就不比较了，只实现这个功能。
#其实词频统计直接用python的Counter对象就行了。

tree=BinarySearchTree()
with open('bible.txt','r',encoding='utf-8') as f:
    file=f.read()
words=list(re.split('\W+',file))
for word in words:
    word=word.lower()
    if tree[word] is None:
        tree[word]=1
    else:
        tree[word]=tree[word]+1
print(tree['god'])