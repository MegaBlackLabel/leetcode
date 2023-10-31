#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [False] * m
        cols = [False] * n

        for r, c in indices:
            rows[r] ^= True
            cols[c] ^= True

        oddRowsCount = rows.count(True)
        oddColsCount = cols.count(True)
        evenRowsCount = m - oddRowsCount
        evenColsCount = n - oddColsCount
    
        return oddRowsCount * evenColsCount + oddColsCount * evenRowsCount
# @lc code=end

