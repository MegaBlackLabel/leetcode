#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for row in matrix:
            minIndex = row.index(min(row))
            if row[minIndex] == max(list(zip(*matrix))[minIndex]):
                return [row[minIndex]]
        return []
# @lc code=end

