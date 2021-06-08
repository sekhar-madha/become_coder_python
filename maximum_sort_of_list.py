def maxsort(data):
    c=1
    maxc=0
    for i in range(len(data)-1):
        if data[i]<=data[i+1]:
            c+=1
            continue
        else:
            if maxc<=c:
                maxc=c
            c=1
            continue
    if data==[]:
        return 0
    if c>maxc:
        return c
    else:
        return maxc
data=list(map(int,input().split()))
print(maxsort(data))
            

