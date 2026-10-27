#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
      
        for i, row in enumerate(mat, start=1):
            for j, value in enumerate(row, start=1):
                prefix_sum[i][j] = (prefix_sum[i - 1][j] + 
                                   prefix_sum[i][j - 1] - 
                                   prefix_sum[i - 1][j - 1] + 
                                   value)
      
        result = [[0] * cols for _ in range(rows)]
      
        for i in range(rows):
            for j in range(cols):
                top_row = max(i - k, 0)
                left_col = max(j - k, 0)
                bottom_row = min(rows - 1, i + k)
                right_col = min(cols - 1, j + k)
              
                result[i][j] = (prefix_sum[bottom_row + 1][right_col + 1] - 
                               prefix_sum[top_row][right_col + 1] - 
                               prefix_sum[bottom_row + 1][left_col] + 
                               prefix_sum[top_row][left_col])
      
        return result
# @lc code=end

