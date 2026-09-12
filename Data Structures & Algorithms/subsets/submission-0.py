class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def sub(index,current):
            if index==len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            sub(index+1,current)
            current.pop()
            sub(index+1,current)
        sub(0,[])
        return result
