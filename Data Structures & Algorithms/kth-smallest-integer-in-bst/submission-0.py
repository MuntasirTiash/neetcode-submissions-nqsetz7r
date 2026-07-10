# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def smallest(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        def delete(root,val):
            if not root:
                return None

            if val > root.val:
                root.right = delete(root.right, val)
            elif val < root.val:
                root.left = delete(root.left,val)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    minval = smallest(root.right)
                    root.val = minval.val
                    root.right = delete(root.right, minval.val)

            return root

        res = 0
        for _ in range(k):
            node = smallest(root)
            res = node.val
            root = delete(root,res)

        return res