#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j],
                              triangle[i + 1][j + 1])

        return triangle[0][0]
# @lc code=end

