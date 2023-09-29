#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summ = sum(arr)
        if summ % 3 != 0:
            return False

        average = summ // 3
        partCount = 0
        partSum = 0

        for a in arr:
            partSum += a
            if partSum == average:
                partCount += 1
                partSum = 0

        return partCount >= 3
    
# @lc code=end

