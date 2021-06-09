def movezeros(data):
    l=len(data)
    for i in range(l):
        if data[i]==0:
            data.remove(0)
            data.insert(l,0)
    return data
data=list(map(int,input().split()))
arr=movezeros(data)
print(*arr)
