#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = 0
        degree = 0
        debut = {}
        count = collections.Counter()

        for i, num in enumerate(nums):
            debut.setdefault(num, i)
            count[num] += 1
            if count[num] > degree:
                degree = count[num]
                ans = i - debut[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - debut[num] + 1)

        return ans
# @lc code=end

