#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [1, 0]
        for c in s:
            w = widths[ord(c)-ord('a')]
            result[1] += w
            if result[1] > 100:
                result[0] += 1
                result[1] = w
        return result
# @lc code=end

