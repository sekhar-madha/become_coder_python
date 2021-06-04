"""
def orig(n,data):
    lst=[]
    count=0
    for i in data:
        if i not in lst:
            lst.append(i)
    for i in range(len(lst)):
        if data[i]==lst[i]:
                   count+=1
    return count
            
n=int(input())
data=list(map(int,input().split()))
count=orig(n,data)
print(count)
"""
def orig(n,data):
    lst=[]
    count=0
    for i in data:
        if i not in lst:
            lst.append(i)
    lst=list(set(lst))
    for i in range(len(lst)):
        if data[i]==lst[i]:
                   count+=1
    return count
            
n=int(input())
data=list(map(int,input().split()))
count=orig(n,data)
print(count)
