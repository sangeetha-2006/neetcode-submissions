# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 0

        def back(root, maximum):

            nonlocal count

            if root is None:
                return

            if root.val >= maximum:
                count += 1
                maximum = root.val

            back(root.left, maximum)
            back(root.right, maximum)

        back(root, root.val)

        return count
        