class Solution:
    def trap(self, height: List[int]) -> int:
        lm = []
        rm = []
        water = 0

        m = 0
        for i in range(len(height)):
            m = max(m, height[i])
            lm.append(m)

        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rm.append(m)

        rm.reverse()

        for i in range(len(height)):
            m = min(lm[i], rm[i])
            water += m - height[i]

        return water