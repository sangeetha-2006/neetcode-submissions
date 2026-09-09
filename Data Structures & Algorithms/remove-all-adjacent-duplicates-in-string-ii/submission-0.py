class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        for i in s:
            stack.append(i)
            if len(stack) >= k and ''.join(stack[-k:]).count(i) == k:
                stack = stack[:-k]

        return ''.join(stack)