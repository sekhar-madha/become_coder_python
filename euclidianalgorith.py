a,b=map(int,input().split())
while True:
    if a>b:
        a,b=b,a
    a,b=a,b%a
    if b==0:
        print(a)
        break
