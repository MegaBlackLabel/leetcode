#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        kMax = 200
        ans = 0
        count = [False] * (kMax + 1)

        for num in nums:
            if num >= 2 * diff and count[num - diff] and count[num - 2 * diff]:
                ans += 1
            count[num] = True

        return ans
# @lc code=end

