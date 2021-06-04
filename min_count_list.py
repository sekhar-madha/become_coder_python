def mincount(mi):
    count=0
    pos=[]
    for i in range(len(data)):
        if mi==data[i]:
            count+=1
            pos.append(i)
    return mi,count,*pos
def minval(data):
    mi=data[0]
    for i in data:
        if i<mi:
            mi=i
    return mi

data=list(map(int,input().split()))
mi=minval(data)
value=mincount(mi)
print(*value)
