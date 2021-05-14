num=int(input())
temp=num
mi=9
ma=0
while num!=0:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(mi,ma)
