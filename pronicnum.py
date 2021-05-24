def pronum(num,a,b):
    for i in range(1,num+1):
        if num==a*b:
            print(True)
            print(i)
            return
        else:
            a+=1
            b+=1
    else:
        print(False)
num=int(input())
pronum(num,1,2)
