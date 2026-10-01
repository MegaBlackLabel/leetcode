#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
      
        total_squares = 0
      
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
              
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],  # top-left diagonal
                        dp[i - 1][j],      # top
                        dp[i][j - 1]       # left
                    ) + 1

                total_squares += dp[i][j]
      
        return total_squares

# @lc code=end

