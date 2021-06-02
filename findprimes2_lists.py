import math as m
def isprime(num):
    if num==0:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1

def findprime(n,data):
    primes=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            primes.append(i)
        else:
            nonprimes.append(i)
    return primes,nonprimes
n=int(input())
data=list(map(int,input().split()))
p,np=findprime(n,data)
print(*p)
print(*np)
        
    
