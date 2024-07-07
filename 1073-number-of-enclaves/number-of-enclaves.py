class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Count the total number of 1s in the grid
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ones += 1

        # Search the border of the grid for 1s and add to DFS stack
        # Flip any 1s to 0s to mark them as visited
        stack = []
        for i in range(m):
            if grid[i][0]:
                stack.append((i, 0))
                grid[i][0] = 0
            if grid[i][n-1]:
                stack.append((i, n - 1))
                grid[i][n-1] = 0
        for i in range(n):
            if grid[0][i]:
                stack.append((0, i))
                grid[0][i] = 0
            if grid[m-1][i]:
                stack.append((m - 1, i))
                grid[m-1][i] = 0

        # DFS to count the number of cells connected to the border
        ct = len(stack)
        while stack:
            x, y = stack.pop()
            # Check neighboring cells
            for x2, y2 in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                # If (x2, y2) is a valid coord and is a 1
                if 0 <= x2 and x2 < m and 0 <= y2 and y2 < n and grid[x2][y2]:
                    # Add to stack, mark as visited, and increment ct
                    stack.append((x2, y2))
                    grid[x2][y2] = 0
                    ct += 1
        
        # Return 1s not connected to the boundary = total 1s - 1s connected to boundary
        return ones - ct