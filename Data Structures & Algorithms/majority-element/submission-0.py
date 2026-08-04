class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        return max(f, key=f.get)
        