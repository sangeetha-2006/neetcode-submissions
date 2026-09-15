class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        used = [False] * len(nums)
        def back(current):
            if len(current)==len(nums):
                result.append(current.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                current.append(nums[i])  
                used[i]=True
                back(current)
                used[i]=False           
                current.pop()   
        back([])
        return result   
        