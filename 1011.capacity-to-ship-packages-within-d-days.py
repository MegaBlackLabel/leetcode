#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity: int) -> bool:
            day_count = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    day_count += 1
                    current_load = 0
                current_load += weight

                if day_count > days:
                    return False

            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left
# @lc code=end

