#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for a in arr:
            count = count + 1 if a % 2 == 1 else 0
            if count == 3:
                return True
        return False
# @lc code=end

