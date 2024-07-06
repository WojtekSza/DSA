# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        ans=[]
        queue=deque([root])
        while queue:
            nodes_in_level=len(queue)
            sub_ans=[]
            for _ in range(nodes_in_level):
                node=queue.popleft()
                sub_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sub_ans)
        return ans