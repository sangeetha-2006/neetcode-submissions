class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!= len(words):
            return False
        pt={}
        wt={}
        for i in range(len(pattern)):
            p=pattern[i]
            w=words[i]
            if p in pt and pt[p] != w:
                return False
            if w in wt and wt[w] != p:
                return False
            pt[p]=w
            wt[w]=p
        return True
        