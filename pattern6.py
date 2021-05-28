n=int(input())
for i in range(1,n+1):
    if i%2:
        for j in range(n,0,-1):
            print(j,end=" ")
        print()
    else:
        for j in range(n):
            print(i,end=" ")
        print()


"""
OUTPUT:

9
9 8 7 6 5 4 3 2 1 
2 2 2 2 2 2 2 2 2 
9 8 7 6 5 4 3 2 1 
4 4 4 4 4 4 4 4 4 
9 8 7 6 5 4 3 2 1 
6 6 6 6 6 6 6 6 6 
9 8 7 6 5 4 3 2 1 
8 8 8 8 8 8 8 8 8 
9 8 7 6 5 4 3 2 1



"""
