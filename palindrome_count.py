def palindromenums(data):
    s,p,c=0,0,1
    count=0
    for i in data:
        temp=i
        s=0
        while i:
            r=i%10
            i=i//10
            s=s*c+r
            c=10
            if temp==s:
                count+=1
    print(count)
data=list(map(int,input().split()))
palindromenums(data)
