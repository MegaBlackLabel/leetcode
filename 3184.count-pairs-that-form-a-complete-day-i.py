#
# @lc app=leetcode id=3184 lang=python3
#
# [3184] Count Pairs That Form a Complete Day I
#

# @lc code=start
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        count = [0] * 24

        for hour in hours:
            ans += count[(24 - hour % 24) % 24]
            count[hour % 24] += 1
            
        return ans
# @lc code=end

