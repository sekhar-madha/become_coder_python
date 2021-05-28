n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,n+1):
            print(j,end=" ")
        print()
    else:
        for j in range(n,0,-1):
            print(j,end=" ")
        print()
        


"""
output:
7
1 2 3 4 5 6 7 
7 6 5 4 3 2 1 
1 2 3 4 5 6 7 
7 6 5 4 3 2 1 
1 2 3 4 5 6 7 
7 6 5 4 3 2 1 
1 2 3 4 5 6 7


"""
