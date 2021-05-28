n=int(input())
for i in range(n):
    for j in range(1,n+1):
        if j%2:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()


"""
OUTPUT:

5
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1


"""
