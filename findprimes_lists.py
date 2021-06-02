def countprimes(n,data):
    lst=[]
    for i in range(len(data)):
        for j in range(2,max(data)+1):
            if data[i]>j:
                if data[i]%j==0:
                    break
        else:
            lst.append(data[i])
    print(*lst)
n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
