class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def back(index):

            if index == len(nums):
                return True

            for i in range(k):

                # Don't exceed target
                if buckets[i] + nums[index] > target:
                    continue

                # Skip identical bucket states
                if i > 0 and buckets[i] == buckets[i - 1]:
                    continue

                buckets[i] += nums[index]

                if back(index + 1):
                    return True

                buckets[i] -= nums[index]

                # If this number couldn't fit in an empty bucket,
                # it won't fit in another empty bucket either.
                if buckets[i] == 0:
                    break

            return False

        return back(0)