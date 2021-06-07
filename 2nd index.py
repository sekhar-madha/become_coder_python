n=int(input())
data=list(map(int,input().split()))
val=int(input())
index=0
if val not in data:
    print(False)
else:
    for i in data:
        if i==val:
            index=data.index(i)
            data.remove(i)
            break
    for i in data:
        if i==val:
            index=data.index(i)
            print(index+1)
            break
    else:
        print(index)
    

