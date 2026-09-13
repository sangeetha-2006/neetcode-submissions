class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def back(index,current):
            if sum(current)==target:
                result.append(current.copy())
                return
            if sum(current) > target:
                return
            for i in range(index,len(nums)):
                current.append(nums[i])
                back(i,current)
                current.pop()
        back(0,[])
        return result

        