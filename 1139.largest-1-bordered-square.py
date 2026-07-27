#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#

# @lc code=start


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] stores (consecutive_left, consecutive_up)
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j][0] = (1 + dp[i][j-1][0]) if j > 0 else 1
                    dp[i][j][1] = (1 + dp[i-1][j][1]) if i > 0 else 1
                    
        # Check squares from maximum possible size downwards
        for sz in range(min(m, n), 0, -1):
            for i in range(m - sz + 1):
                for j in range(n - sz + 1):
                    r, c = i + sz - 1, j + sz - 1
                    # Validate all four borders have length >= sz
                    if (dp[r][c][0] >= sz and dp[r][c][1] >= sz and 
                        dp[r][j][1] >= sz and dp[i][c][0] >= sz):
                        return sz * sz
        return 0
# @lc code=end

