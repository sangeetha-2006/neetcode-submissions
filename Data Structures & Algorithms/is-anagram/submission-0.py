class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_text = "".join(sorted(s))
        sorted_text1 = "".join(sorted(t))
        if len(s)!=len(t):
            return False
        else:
            return sorted_text==sorted_text1