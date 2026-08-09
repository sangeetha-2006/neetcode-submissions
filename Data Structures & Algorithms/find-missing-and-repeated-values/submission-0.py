class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        r=[]
        for x in grid:
            r.extend(x)
        r.sort()
        for i in r:
            if r.count(i)>1:
                ans.append(i)
                break
        for  i in range(1,len(r)+1):
            if i not in r:
                ans.append(i)
        return ans
        