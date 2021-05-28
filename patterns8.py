n=int(input())
for i in range(n):
    if i%2:
        temp=0
    else:
        temp=1
    for j in range(n):
        print(temp,end=" ")
        if temp==0:
            temp=1
        else:
            temp=0
    print()

"""
OUTPUT:


5
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1


"""
