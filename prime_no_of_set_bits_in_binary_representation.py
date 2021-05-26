class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        d=0
        temp=left
        while left:
            r=left%2
            left=left//2
            if r==1:
                c+=1
            if left==0 and c>=1:
                if c==1:
                    d-=1
                for i in range(2,c):
                    if c%i==0:
                        break
                else:
                    d+=1
                temp=temp+1
                left=temp
                c=0
            if left>right:
                break
        return d
    
