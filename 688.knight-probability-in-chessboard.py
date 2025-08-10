#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1.0
        
        directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
                      (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8.0
            dp = new_dp
        
        return sum(sum(row) for row in dp)
# @lc code=end

