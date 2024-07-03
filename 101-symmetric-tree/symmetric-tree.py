# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def leftCheck(root,vals):
            if root is None:
                vals.append(None)
                return
            vals.append(root.val)
            leftCheck(root.left,vals)
            leftCheck(root.right,vals)
            return vals
        def rightCheck(root,vals):
            if root is None:
                vals.append(None)
                return
            vals.append(root.val)
            rightCheck(root.right,vals)
            rightCheck(root.left,vals)
            return vals
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True    
        if root.left and root.right:
            left=leftCheck(root.left,[])
            right=rightCheck(root.right,[])
            return left==right
        else:
            return False