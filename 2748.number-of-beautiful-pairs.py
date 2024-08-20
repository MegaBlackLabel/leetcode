#
# @lc app=leetcode id=2748 lang=python3
#
# [2748] Number of Beautiful Pairs
#

# @lc code=start
import math
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def firstDigit(num: int) -> int:
            return int(str(num)[0])

        def lastDigit(num: int) -> int:
            return num % 10

        return sum(math.gcd(firstDigit(nums[i]), lastDigit(nums[j])) == 1
               for i in range(len(nums))
               for j in range(i + 1, len(nums)))
# @lc code=end

