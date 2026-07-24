class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        p=0
        for i in prices:
            if i<m:
                m=i
            else:
                p=max(p,i-m)
        return p

        