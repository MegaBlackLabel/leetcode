#
# @lc app=leetcode id=2784 lang=python3
#
# [2784] Check if Array is Good
#

# @lc code=start
import collections
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        count = collections.Counter(nums)
    
        return all(count[i] == 1 for i in range(1, n)) and count[n] == 2
# @lc code=end

