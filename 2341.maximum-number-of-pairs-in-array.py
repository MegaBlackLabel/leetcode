#
# @lc app=leetcode id=2341 lang=python3
#
# [2341] Maximum Number of Pairs in Array
#

# @lc code=start
import collections
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0] * 2
        count = collections.Counter(nums)

        for i in range(101):
            ans[0] += count[i] // 2
            ans[1] += count[i] & 1

        return ans
    
# @lc code=end

