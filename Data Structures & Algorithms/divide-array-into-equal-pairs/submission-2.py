class Solution:

    def divideArray(self, nums: List[int]) -> bool:

        l = []

        nums.sort()

        r = len(nums) // 2

        for i in range(0, len(nums), 2):

            if nums[i] == nums[i + 1]:
                l.append(nums[i])

        if r == len(l):
            return True

        return False