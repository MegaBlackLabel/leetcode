#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            if 9 < num < 100 or 999 < num < 10000 or num == 100000:
                ans += 1

        return ans
# @lc code=end

