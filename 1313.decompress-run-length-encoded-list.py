#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(0, len(nums), 2):
            ans += [nums[i + 1]] * nums[i]

        return ans
# @lc code=end

