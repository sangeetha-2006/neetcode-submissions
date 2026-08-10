class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incount = 1
        decount = 1
        ans = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                incount += 1
            else:
                incount = 1

            if nums[i] < nums[i - 1]:
                decount += 1
            else:
                decount = 1

            ans = max(ans, incount, decount)

        return ans