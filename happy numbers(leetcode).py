class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        c=0
        while n:
            r=n%10
            n=n//10
            s=s+r**2
            if n==0 and s>1:
                n=s
                s=0
                c+=1
                if c>10:
                    return False
            if n==0 and s==1:
                return True
                
