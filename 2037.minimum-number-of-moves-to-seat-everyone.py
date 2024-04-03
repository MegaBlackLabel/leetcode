#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
         return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))
# @lc code=end

