class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def back(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if nums[i] in current:
                    continue

                current.append(nums[i])

                back(current)

                current.pop()

        back([])

        return result