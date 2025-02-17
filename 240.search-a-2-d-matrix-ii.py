#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1

        return False
# @lc code=end

