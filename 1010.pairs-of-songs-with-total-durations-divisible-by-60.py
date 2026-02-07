#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = [0] * 60
        result = 0

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            result += count[complement]
            count[remainder] += 1

        return result
# @lc code=end

