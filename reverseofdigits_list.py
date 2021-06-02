def reversedigits(data):
    s=0
    c=1
    p=0
    for i in data:
        while i:
            r=i%10
            i=i//10
            s=s*c+r
            c=10
            if i==0:
                data[p]=s
                p+=1
                s=0
    return data
    
data=list(map(int,input().split()))
reversedigits(data)
print(*data)
