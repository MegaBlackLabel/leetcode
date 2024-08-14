#
# @lc app=leetcode id=2717 lang=python3
#
# [2717] Semi-Ordered Permutation
#

# @lc code=start
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        index1 = nums.index(1)
        indexN = nums.index(n)
        return index1 + (n - 1 - indexN) - int(index1 > indexN)
# @lc code=end

