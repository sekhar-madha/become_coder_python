def maxsort(data):
    c=1
    maxc=0
    sets=0
    for i in range(len(data)-1):
        if data[i]<=data[i+1]:
            c+=1
            continue
        else:
            if maxc<=c:
                maxc=c
                sets+=1
            c=1
            sets+=1
            continue
    if data==[]:
        return 0
    if c>maxc:
        return sets
    else:
        return sets
data=list(map(int,input().split()))
print(maxsort(data))
            


