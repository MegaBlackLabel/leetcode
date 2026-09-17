#
# @lc app=leetcode id=1253 lang=python3
#
# [1253] Reconstruct a 2-Row Binary Matrix
#

# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        matrix = [[0] * n for _ in range(2)]
      
        upper_remaining = upper
        lower_remaining = lower
      
        for col_idx, col_sum in enumerate(colsum):
            if col_sum == 2:
                matrix[0][col_idx] = 1
                matrix[1][col_idx] = 1
                upper_remaining -= 1
                lower_remaining -= 1
              
            elif col_sum == 1:
                if upper_remaining > lower_remaining:
                    matrix[0][col_idx] = 1
                    upper_remaining -= 1
                else:
                    matrix[1][col_idx] = 1
                    lower_remaining -= 1
          
            if upper_remaining < 0 or lower_remaining < 0:
                return []
      
        if upper_remaining == 0 and lower_remaining == 0:
            return matrix
        else:
            return []
# @lc code=end

