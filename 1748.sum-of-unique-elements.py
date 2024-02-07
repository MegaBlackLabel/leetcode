#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
import collections
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, freq in collections.Counter(nums).items() if freq == 1)
# @lc code=end

