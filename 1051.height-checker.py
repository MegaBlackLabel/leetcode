#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        currentHeight = 1
        count = [0] * 101

        for height in heights:
            count[height] += 1

        for height in heights:
            while count[currentHeight] == 0:
                currentHeight += 1
            if height != currentHeight:
                ans += 1
            count[currentHeight] -= 1

        return ans
# @lc code=end

