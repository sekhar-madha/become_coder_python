def secondlargest(n,data):
    L=1
    SL=0
    data.sort()
    for i in data:
        if i>L:
            SL=L
            L=i
    return SL
n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))
            
    
    
