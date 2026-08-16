class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        arr=[]
        while l<r:
            if numbers[l]+numbers[r]==target:
                arr.append(l+1)
                arr.append(r+1)
                return arr
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1

        return arr
        