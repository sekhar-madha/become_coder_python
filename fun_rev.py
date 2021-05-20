def rev(num,rn):
    if num==0:
        print(rn)
        return
    rn=rn*10+num%10
    rev(num//10,rn)
num=int(input())
rev(num,0)

