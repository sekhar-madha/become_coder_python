def leastcount(data):
    n=9
    lst=[]
    for i in data:
        if data.count(i)<n:
            n=data.count(i)
    for i in data:
        if data.count(i)==n:
            lst.append(i)
            
    print(n)
    return lst
            
data=list(map(int,input().split()))
lc=leastcount(data)
print(*lc)
