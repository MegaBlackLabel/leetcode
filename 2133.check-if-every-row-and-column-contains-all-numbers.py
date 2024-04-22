#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(min(len(set(row)), len(set(col))) == len(matrix)
               for row, col in zip(matrix, zip(*matrix)))
# @lc code=end

