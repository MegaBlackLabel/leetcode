#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        numToIndex = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            target = num + k
            if target in numToIndex and numToIndex[target] != i:
                ans += 1
                del numToIndex[target]

        return ans
# @lc code=end

