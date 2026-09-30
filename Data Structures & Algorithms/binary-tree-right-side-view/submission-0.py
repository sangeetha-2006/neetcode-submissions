# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result=[]
        def right(root,r):
            if root is None:
                return 
            if r==len(result):
                result.append(root.val)
            right(root.right,r+1)
            right(root.left,r+1)
        right(root,0)
        return result
