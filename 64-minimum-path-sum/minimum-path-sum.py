class Solution:
    """My Bottom-up tabulation solution"""
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                left = grid[i-1][j] if i > 0 else float('inf')
                up = grid[i][j-1] if j > 0 else float('inf')
                grid[i][j] += min(left, up)
        return grid[-1][-1]