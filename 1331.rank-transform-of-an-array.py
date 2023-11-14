#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for a in sorted(arr):
            if a not in rank:
                rank[a] = len(rank) + 1

        return map(rank.get, arr)
# @lc code=end

