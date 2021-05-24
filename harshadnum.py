def isharshadnum(num):
    c=0
    temp=num
    while num!=0:
        r=num%10
        num=num//10
        c=c+r
    if temp%c==0:
        print(True)
    else:
        print(False)
num=int(input())
isharshadnum(num)
            
        
