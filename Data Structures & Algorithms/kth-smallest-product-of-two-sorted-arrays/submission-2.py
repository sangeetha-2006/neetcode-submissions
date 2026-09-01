class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        dp = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp.append(nums1[i] * nums2[j])

        dp.sort()

        return dp[k - 1]