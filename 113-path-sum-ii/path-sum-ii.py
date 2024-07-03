# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def traverseRoot(root,curr,summ,targetSum):
            if root is None:
                return []
            summ+=root.val
            curr=curr.copy()
            curr.append(root.val)
            if root.left is None and root.right is None:
                if summ==targetSum:
                    ans.append(curr)
            traverseRoot(root.left,curr,summ,targetSum)
            traverseRoot(root.right,curr,summ,targetSum)
        traverseRoot(root,[],0,targetSum)
        return [] if ans==[[]] else ans
        
        