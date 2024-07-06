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
                print(node.val)
                print(level)
                if level%2!=0:
                    print('level%2!=0')
                    if node.val%2==0:
                        return False
                        print('--->1')
                    if sub_sum and sub_sum[-1]>=node.val:
                        print('--->2')
                        return False
                elif level%2==0:
                    print('level%2==0')
                    if node.val%2!=0:
                        print('--->3')                        
                        return False
                    if sub_sum and sub_sum[-1]<=node.val:
                        print('--->4')
                        return False
                sub_sum.append(node.val)
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            level+=1
        return True       
                


        