num=int(input())
temp=num
c,s=0,0
while temp:
    r=temp%10
    temp=temp//10
    c+=1
temp=num
while num:
    r=num%10
    s=s+r**c
    num=num//10
if s==temp:
    print(temp," is an Armstrong number")
else:
    print(temp,"is not an Armstrong number")
