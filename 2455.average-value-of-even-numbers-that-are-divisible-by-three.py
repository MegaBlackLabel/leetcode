#
# @lc app=leetcode id=2455 lang=python3
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        summ = 0
        count = 0

        for num in nums:
            if num % 6 == 0:
                summ += num
                count += 1

        return 0 if count == 0 else summ // count
# @lc code=end

