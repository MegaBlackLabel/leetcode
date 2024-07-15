#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for num in nums for c in str(num)]
# @lc code=end

