class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        def back(index,current):
            result.append(current.copy())
            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                back(i+1,current)
                current.pop()
        back(0,[])
        return result
        