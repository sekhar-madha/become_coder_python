a,b=map(int,input().split())
d=2
res=1
while True:
    if a%d==0 and b%d==0:
        res=res*d
        a=a//d
        b=b//d
    else:
        d=d+1
    if a<d or b<d:
        break
print(res*a*b)
        
        
