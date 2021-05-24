def gcd(a,b):
    if a>b:
        a,b=b,a
    a,b=a,b%a
    if b==0:
        print(a)
        return
    else:
        gcd(a,b)
a,b=map(int,input().split())
gcd(a,b)
