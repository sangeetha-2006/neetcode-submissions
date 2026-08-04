class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        max_odd = 0
        min_even = float('inf')   # changed

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for count in freq.values():
            if count % 2 == 0:
                min_even = min(min_even, count)   # changed
            else:
                max_odd = max(max_odd, count)

        return max_odd - min_even