#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0

        prevEvenSum = 0
        prevOddSum = 0

        for i, a in enumerate(arr):
            currEvenSum = prevOddSum + ((i + 1) // 2) * a
            currOddSum = prevEvenSum + (i // 2 + 1) * a
            ans += currOddSum
            prevEvenSum = currEvenSum
            prevOddSum = currOddSum

        return ans
# @lc code=end

