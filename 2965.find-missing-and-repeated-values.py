#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = [1] + [0] * len(grid)**2  # padding for 1-indexed

        for row in grid:
            for num in row:
                count[num] += 1

        return [count.index(2), count.index(0)]
# @lc code=end

