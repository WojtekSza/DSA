class Solution:
	def longestZigZag(self, root: Optional[TreeNode]) -> int:

		self.result = 0

		def DFS(node, current_max_path, direction):

			if node != None:

				self.result = max(self.result, current_max_path)

				if direction:
					DFS(node.right , current_max_path + 1 , False)
					DFS(node.left , 1 , True)

				else:
					DFS(node.left , current_max_path + 1 , True)
					DFS(node.right , 1 , False)

		if root.left:
			DFS(root.left , 1 , True)

		if root.right:
			DFS(root.right , 1 , False)

		return self.result
		