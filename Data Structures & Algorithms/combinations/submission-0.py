class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def back(index,current):
            if len(current) == k:
                result.append(current.copy())
                return 
            for i in range(index, n + 1):
                current.append(i)
                back(i+1,current)
                current.pop()
        back(1,[])
        return result
