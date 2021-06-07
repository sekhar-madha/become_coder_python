def secondmax(n,data):
    data.sort()
    print(data[-2])
n=int(input())
data=list(map(int,input().split()))
secondmax(n,data)
            
