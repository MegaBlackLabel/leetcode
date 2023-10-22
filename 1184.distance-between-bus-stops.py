#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
#

# @lc code=start
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        counterclockwise = 0

        if start > destination:
            start, destination = destination, start

        for i, d in enumerate(distance):
            if i >= start and i < destination:
                clockwise += d
            else:
                counterclockwise += d

        return min(clockwise, counterclockwise)
# @lc code=end

