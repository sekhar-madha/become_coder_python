import math as m
num=int(input())
c=0
n=int(m.sqrt(num))
for i in range(1,n+1):
    if num%i==0:
        if i!=(num//i):
            c+=2
        else:
            c+=1
print(c)
        
