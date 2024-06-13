#
# @lc app=leetcode id=2399 lang=python3
#
# [2399] Check Distances Between Same Letters
#

# @lc code=start
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        firstSeenIndex = [-1] * 26

        for i, c in enumerate(s):
            j = ord(c) - ord('a')
            prevIndex = firstSeenIndex[j]
            if prevIndex != -1 and i - prevIndex - 1 != distance[j]:
                return False
            firstSeenIndex[j] = i

        return True
# @lc code=end

