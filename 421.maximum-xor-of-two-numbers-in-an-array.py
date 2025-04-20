#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
import math
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxNum = max(nums)
        if maxNum == 0:
            return 0
    
        maxBit = int(math.log2(maxNum))
        ans = 0
        prefixMask = 0 

        for i in range(maxBit, -1, -1):
            prefixMask |= 1 << i
            prefixes = set([num & prefixMask for num in nums])
            candidate = ans | 1 << i
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    ans = candidate
                    break

        return ans

# @lc code=end

