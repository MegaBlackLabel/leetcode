#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
import collections
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        kMax = 100
        count = collections.Counter(nums)

        for i in range(1, kMax + 1):
            count[i] += count[i - 1]

        return [0 if num == 0 else count[num - 1] for num in nums]
# @lc code=end

