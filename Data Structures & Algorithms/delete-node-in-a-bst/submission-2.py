# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.remove(root,key)

    def remove(self,root, key):
        if not root:
            return None

        if key > root.val:
            root.right = self.remove(root.right, key)
        elif key < root.val:
            root.left = self.remove(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minval = self.findminValue(root.right)
                root.val = minval.val
                root.right = self.remove(root.right,minval.val)

        return root

    def findminValue(self,root):
        curr = root

        while curr and curr.left:
            curr = curr.left
        
        return curr

        
    