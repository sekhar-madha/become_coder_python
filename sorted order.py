def sortedorder(data):
    lst=[]
    revlst=[]
    for i in range(len(data)):
        lst.append(data[i])
        revlst.append(data[i])
    lst.sort()
    revlst.sort()
    revlst.reverse()
    if data==lst or data==revlst:
        return True
    else:
        return False
data=list(map(int,input().split()))
print(sortedorder(data))
