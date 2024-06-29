#
# @lc app=leetcode id=2475 lang=python3
#
# [2475] Number of Unequal Triplets in Array
#

# @lc code=start
import collections
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        prev = 0
        next = len(nums)

        for freq in collections.Counter(nums).values():
            next -= freq
            ans += prev * freq * next
            prev += freq

        return ans
# @lc code=end

