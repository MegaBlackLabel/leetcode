#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 2)
        
        for first, last, seats in bookings:
            res[first] += seats
            res[last + 1] -= seats
            
        for i in range(1, n + 1):
            res[i] += res[i - 1]
            
        return res[1:n + 1]
# @lc code=end

