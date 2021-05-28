n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(n):
            print(i,end=" ")
        print()
    else:
        for j in range(1,n+1):
            print(j,end=" ")
        print()


"""
output:

9
1 2 3 4 5 6 7 8 9 
2 2 2 2 2 2 2 2 2 
1 2 3 4 5 6 7 8 9 
4 4 4 4 4 4 4 4 4 
1 2 3 4 5 6 7 8 9 
6 6 6 6 6 6 6 6 6 
1 2 3 4 5 6 7 8 9 
8 8 8 8 8 8 8 8 8 
1 2 3 4 5 6 7 8 9


"""
