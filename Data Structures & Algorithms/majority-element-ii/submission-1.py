class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr={}
        a=[]
        for num in nums:
            if num in arr:
                arr[num] += 1
            else:
                arr[num] = 1
        for i in arr:
            if arr[i]>len(nums) // 3:
                a.append(i)
        return a
                