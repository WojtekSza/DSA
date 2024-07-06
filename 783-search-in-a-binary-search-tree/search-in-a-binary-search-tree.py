class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.right and root.val<val: 
            root=root.right
            return self.searchBST(root,val)
        elif root.left and root.val>val: 
            root=root.left
            return self.searchBST(root,val)
        elif root.val==val: 
            return root
        return None