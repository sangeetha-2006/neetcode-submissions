class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        m = nums[0]

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += nums[i + 1]
            else:
                m = max(m, curr)
                curr = nums[i + 1]

        return max(m, curr)