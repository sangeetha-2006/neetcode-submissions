class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(ch) for ch in s]
        score = 0
        for i in range(len(ascii_values) - 1):
            score += abs(ascii_values[i + 1] - ascii_values[i])
        return score
