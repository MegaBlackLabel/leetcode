#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0

        for batteryPercentage in batteryPercentages:
            if batteryPercentage - ans > 0:
                ans += 1

        return ans
# @lc code=end

