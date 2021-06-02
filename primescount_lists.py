def countprimes(n,data):
    pc=0
    for i in range(len(data)):
        for j in range(2,max(data)+1):
            if data[i]>j:
                if data[i]%j==0:
                    break
        else:
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
print(pc)
