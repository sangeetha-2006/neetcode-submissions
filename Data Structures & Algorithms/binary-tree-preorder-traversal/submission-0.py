class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(node):
            if node is None:
                return

            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ans