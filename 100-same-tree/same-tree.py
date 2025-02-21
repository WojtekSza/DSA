# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val==q.val:
            if (p.left is None and q.left is None) and (p.right is None and q.right is None ):
                return True
            elif p.val!=q.val:
                return False
            left=self.isSameTree(p.left,q.left)
            right=self.isSameTree(p.right,q.right)
        else:
            return False
        return left and right