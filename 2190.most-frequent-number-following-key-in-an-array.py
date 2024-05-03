#
# @lc app=leetcode id=2190 lang=python3
#
# [2190] Most Frequent Number Following Key In an Array
#

# @lc code=start
import collections
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = collections.Counter()

        for a, b in zip(nums, nums[1:]):
            if a == key:
                count[b] += 1

        return max(count, key=lambda k: count[k])
# @lc code=end

