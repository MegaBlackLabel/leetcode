#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSizesSet = set(bobSizes)

        for aliceSize in aliceSizes:
            target = aliceSize - diff
            if target in bobSizesSet:
                return [aliceSize, target]
# @lc code=end

