#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0

        for boxes, units in sorted(boxTypes, key=lambda x: -x[1]):
            if boxes >= truckSize:
                return ans + truckSize * units
            ans += boxes * units
            truckSize -= boxes

        return ans
# @lc code=end

