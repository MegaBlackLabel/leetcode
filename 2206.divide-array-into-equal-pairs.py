#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
import collections
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(value % 2 == 0 for value in collections.Counter(nums).values())
# @lc code=end

