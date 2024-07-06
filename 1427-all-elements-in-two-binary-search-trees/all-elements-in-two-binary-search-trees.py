# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        data=[]
        def dfs(root):
            if root is None:
                return root
            dfs(root.left)
            data.append(root.val)
            dfs(root.right)
        dfs(root1)
        dfs(root2)
        data.sort()
        return data
        