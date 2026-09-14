class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def back(index,current):
            if sum(current)==target:
                result.append(current.copy())
                return
            if sum(current)>target:
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                current.append(candidates[i])
                back(i+1,current)
                current.pop()
        back(0,[])
        return result
        