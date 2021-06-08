def bouncyarray(data):
    count=0
    c=0
    for i in range(len(data)-1):
        if i%2!=0:
            if data[i]<data[i+1]:
                count+=1
                continue
            else :
                c+=1
                continue
        else:
            if data[i]>data[i+1]:
                count+=1
                continue
            else :
                c+=1
                continue
    if count==len(data)-1:
        return count==len(data)-1
    else:
        return c==len(data)-1
data=list(map(int,input().split()))
print(bouncyarray(data))
        
