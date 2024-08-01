#
# @lc app=leetcode id=2644 lang=python3
#
# [2644] Find the Maximum Divisibility Score
#

# @lc code=start
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = -1
        maxScore = -1

        for divisor in divisors:
            score = sum([1 for num in nums if num % divisor == 0])
            if score > maxScore:
                ans = divisor
                maxScore = score
            elif score == maxScore:
                ans = min(ans, divisor)

        return ans
# @lc code=end

