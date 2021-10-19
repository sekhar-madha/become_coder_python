s=input()
r=int(input())
rs,f="",0
t=r+(r-2)
le=len(s)
if le<=1:
    print(s)
    exit
while r!=0:
    l=r+(r-2)
    if r==1:
        l=t
    for i in s[f::l]:
        rs+=i
    r-=1
    f+=1
print(rs)
