def maxones(data):
    count=0
    maxc=0
    for i in range(len(data)):
        if data[i]==1:
            count+=1
            continue
        else:
            if maxc<=count:
                maxc=count
            count=0
    if count>maxc:
        return count
    else:
        return maxc
            
data=list(map(int,input().split()))
print(maxones(data))
