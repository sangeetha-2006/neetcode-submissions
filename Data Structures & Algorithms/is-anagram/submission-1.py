class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1={}
        c2={}
        for ch in s.lower():
            if not  ch.isspace():
                c1[ch]=c1.get(ch,0)+1
        for ch in t.lower():
            if not  ch.isspace():
                c2[ch]=c2.get(ch,0)+1
        return c1==c2
