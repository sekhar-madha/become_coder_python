num=int(input())
temp=num
mi=9
ma=0
c=0
d=0
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    elif r<mi:
        mi=r
while temp:
    r=temp%10
    temp=temp//10
    if r==ma:
        c=c+1
    elif r==mi:
        d=d+1
print(d,c)
