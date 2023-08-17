#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

# @lc code=start
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        ans = []
        i = 0
        j = 0

        while i < n:
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                ans.append([i, j - 1])
            i = j

        return ans
# @lc code=end

