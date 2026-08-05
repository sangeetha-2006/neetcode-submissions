class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        last_word = s.split()[-1]
        for i in last_word:
            count+=1
        return count
        