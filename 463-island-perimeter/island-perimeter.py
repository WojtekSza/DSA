class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, 1)]

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                
                total = 4
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if not (0 <= nx < M) or not (0 <= ny < N):
                        continue

                    if grid[nx][ny] == 0:
                        continue
                    total -= 1
                
                ans += total
        return ans

