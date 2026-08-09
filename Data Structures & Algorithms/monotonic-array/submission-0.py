class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    inc = False

                if nums[i] < nums[j]:
                    dec = False

        return inc or dec