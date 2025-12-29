#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#

# @lc code=start
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        max_time = -1

        # Generate all permutations of the array
        from itertools import permutations
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            # Check if the time is valid
            if 0 <= hours < 24 and 0 <= minutes < 60:
                total_minutes = hours * 60 + minutes
                max_time = max(max_time, total_minutes)

        if max_time == -1:
            return ""

        max_hours = max_time // 60
        max_minutes = max_time % 60
        return f"{max_hours:02}:{max_minutes:02}"

# @lc code=end

