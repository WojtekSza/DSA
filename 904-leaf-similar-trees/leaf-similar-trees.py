# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafs(root,seq):
            if root is None:
                return seq
            if root.left is None and root.right is None:
                seq.append(root.val)
            getLeafs(root.left,seq)
            getLeafs(root.right,seq)
            return seq
        seq1=getLeafs(root1,[])
        seq2=getLeafs(root2,[])
        return seq1==seq2