def isNeighbour(N):
    ##Your code here
    r=range(-2,3)
    l=list(map(lambda x:x+N,r))
    for i in l:
        if i%10==0:
            return True
            break
        else:
            pass
    else:
        return False
