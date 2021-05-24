def lcm(a,b,res=1,d=2):
    if a%d==0 and b%d==0:
        res=res*d
    else:
        d=d+1
        print(d)
    if d>a or d>b:
        return
    lcm(a//d,b//d,res,d)
a,b=map(int,input().split())
a=lcm(a,b)
print(a)        
    
