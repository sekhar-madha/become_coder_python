"""
n=int(input())
for i in range(n,0,-1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
