num=int(input())
s=0
for i in range(1,num):
    if num%i==0:
        s=s+i
if s==num:
    print("perfect number")
else:
    print("not a perfect number")
