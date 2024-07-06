# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root
        queue=deque([root])
        ans=[]
        sum_max=float("-inf")
        while queue:
            sub_sum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                sub_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sub_sum)
            sum_max=max(sum_max,sub_sum)
        for i,val in enumerate(ans):
            if val==sum_max:
                return i+1
        return 0

