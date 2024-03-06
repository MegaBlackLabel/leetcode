#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
# @lc code=end

