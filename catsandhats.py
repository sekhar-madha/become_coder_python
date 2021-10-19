s=input()
cc,hc=0,0
i,l=0,len(s)
k,r=0,0
t=""
while i<l:
    if s[i]=="c":
        k=1
        t=s[i]
    elif k!=0:
        r+=1
        t+=s[i]
    else:
        pass
    if r==2:
        if t=="cat":
            cc+=1
            t=""
            r=0
            k=0
        else:
            t=""
            r=0
            k=0
    print(i,t)
    i+=1
i,k,r=0,0,0
while i<l:
    if s[i]=="h":
        k=1
        t=s[i]
    elif k!=0:
        r+=1
        t+=s[i]
    else:
        pass
    if r==2:
        if t=="hat":
            hc+=1
            t=""
            r=0
            k=0
        else:
            t=""
            r=0
            k=0
    print(i,t)
    i+=1
print(cc,hc)
