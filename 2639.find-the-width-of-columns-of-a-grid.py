#
# @lc app=leetcode id=2639 lang=python3
#
# [2639] Find the Width of Columns of a Grid
#

# @lc code=start
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(map(len, map(str, col))) for col in zip(*grid)]
# @lc code=end

