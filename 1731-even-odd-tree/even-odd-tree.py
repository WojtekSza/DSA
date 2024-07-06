# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root])
        level=1
        while queue:
            sub_sum=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                if level%2!=0:
                    if node.val%2==0:
                        return False
                    if sub_sum and sub_sum[-1]>=node.val:
                        return False
                elif level%2==0:
                    if node.val%2!=0:                        
                        return False
                    if sub_sum and sub_sum[-1]<=node.val:
                        return False
                sub_sum.append(node.val)
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            level+=1
        return True       
                


        