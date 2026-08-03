import math
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        a=0
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            elif m*m<x:
                a=m
                l=m+1
            else:
                r=m-1
        return a