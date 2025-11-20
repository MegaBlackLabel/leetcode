#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#

# @lc code=start
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        result = []
        total_cells = rows * cols
        steps = 0
        r, c = rStart, cStart

        while len(result) < total_cells:

            for _ in range(steps + 1):
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                c += 1

            for _ in range(steps + 1):
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                r += 1
            steps += 1

            for _ in range(steps + 1):
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                c -= 1

            for _ in range(steps + 1):
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                r -= 1
            steps += 1

        return result
# @lc code=end

