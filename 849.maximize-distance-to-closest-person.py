#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        max_distance = 0
        last_occupied = -1
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if last_occupied == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, (i - last_occupied) // 2)
                last_occupied = i

        if seats[n - 1] == 0:
            max_distance = max(max_distance, n - 1 - last_occupied)

        return max_distance
# @lc code=end

