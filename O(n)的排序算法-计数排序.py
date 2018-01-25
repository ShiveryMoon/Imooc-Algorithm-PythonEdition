#算法解析见http://blog.csdn.net/fynjy/article/details/46715289

def countSort(alist, maximum):
    length = len(alist)
    clist = [0]*(maximum+1)
    blist = [0]*length
    for i in range(length):
        clist[alist[i]] += 1
    for i in range(1, len(clist)):
        clist[i] = clist[i] + clist[i-1]
    for i in range(length):
        blist[clist[alist[i]]-1] = alist[i]
        clist[alist[i]] -= 1
    return blist

b=countSort([1,3,3,2,5,3,0,0,6,4,2,4,5], 6)
print(b)