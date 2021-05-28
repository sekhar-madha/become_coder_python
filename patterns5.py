n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1:
            print(i,end=" ")
            continue
        print(j,end=" ")
    print()



"""
OUTPUT:

7
1 2 3 4 5 6 7 
2 2 3 4 5 6 7 
3 2 3 4 5 6 7 
4 2 3 4 5 6 7 
5 2 3 4 5 6 7 
6 2 3 4 5 6 7 
7 2 3 4 5 6 7


"""
