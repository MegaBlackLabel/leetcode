#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for num in range(1, 7):
            if all(num in pair for pair in zip(tops, bottoms)):
                return len(tops) - max(tops.count(num), bottoms.count(num))
        return -1
# @lc code=end

