#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        currAltitude = 0
    
        for g in gain:
            currAltitude += g
            ans = max(ans, currAltitude)
    
        return ans
# @lc code=end

