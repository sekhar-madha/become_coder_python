def revmin(n,mi):
    s=0
    temp=mi
    while mi:
        r=mi%10
        mi=mi//10
        s=s*10+r
    for i in data:
        if s<i:
            if i==data[n-1]:
                print("superlative minimum")
    else:
        print(temp)
                
                       
def minval(n,data):
    mi=data[0]
    for i in data:
        if i<mi:
            mi=i
    revmin(n,mi)
    
n=int(input())
data=list(map(int,input().split()))
minval(n,data)
