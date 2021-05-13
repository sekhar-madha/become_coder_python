num=int(input())
temp=num
f=l=0
nn=0
c=0
d=0
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
c=d=c-1
if num>0:
    f=num//pow(10,c)
    l=num%10
while num:
    r=num%10
    num=num//10
    if c==d:
        r=f
    elif c==0:
        r=l
    nn=nn*10+r
    c=c-1
print(nn)
    
    
    
    
