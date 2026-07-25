class Solution:
    def replaceElements(self, arr: Liset[int]) -> List[int]:
        r=-1
        for i in range(len(arr)-1,-1,-1):
            p=arr[i]
            arr[i]=r
            r=max(p,r)
        return arr