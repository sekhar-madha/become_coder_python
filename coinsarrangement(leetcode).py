n=int(input())
count=1
c=0
i=1
while n!=0:
    if i==count:
        c+=1
        count+=1
        i=0
        n=n-1
    else:
        n-=1
    i=i+1
        
print(c)
