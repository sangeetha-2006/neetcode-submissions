class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def back(current,open,close):
            if len(current)==2*n:
                result.append("".join(current))
                return
            if open<n:
                current.append("(")
                back(current,open+1,close)
                current.pop()
            if close<open:
                current.append(")")
                back(current,open,close+1)
                current.pop()
        back([],0,0)
        return result
        