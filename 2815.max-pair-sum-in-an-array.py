#
# @lc app=leetcode id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        maxNum = [0] * 10

        def getMaxDigit(num: int) -> int:
            maxDigit = 0
            while num > 0:
                maxDigit = max(maxDigit, num % 10)
                num //= 10
            return maxDigit

        for num in nums:
            d = getMaxDigit(num)
            if maxNum[d] > 0:
                ans = max(ans, num + maxNum[d])
            maxNum[d] = max(maxNum[d], num)

        return -1 if ans == 0 else ans
# @lc code=end

