def doge_count(str):
    count = 0
    s=""
    c=0
    ##Your code here
    l=["doae","dobe","doce","dode","dofe","doee","doge","dohe","doie","doje","doke","dole","dome","done","dooe","dope","doqe","dore","dose","dote","doue","dove","dowe","doxe","doye","doze"]
    for i in str:
        if i=="d":
            c=1
            s=i
        else:
            s+=i
            c+=1
        if c==4:
            if s in l:
                count+=1
                s=""
                c=0
            else:
                c=0
                s=""
    p=str.count("dode")
    count=count+p
                
    return count
