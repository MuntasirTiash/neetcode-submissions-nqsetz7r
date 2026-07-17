class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            self.max_diameter = max(self.max_diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter