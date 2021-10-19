class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h=heights
        sp,i,k=0,0,0
        l=[0]*len(h)
        f=1
        t=max(h)
        if h.count(t)==len(h):
            return t*len(h)
        while i<len(h):
            sp=h[i]
            k=i+1
            while k<len(h):
                if sp<=h[k]:
                    f+=1
                    k+=1
                    continue
                else:
                    break
            k=i-1
            while k>-1:
                if sp<=h[k]:
                    f+=1
                    k-=1
                    continue
                else:
                    break
            l[i]=sp*f
            f=1
            i+=1
        return max(l)
                    
