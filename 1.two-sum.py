#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            search_key = target - num
            if search_key not in hashmap:
                hashmap[num] = i
            else:
                return [i, hashmap[search_key]]


# @lc code=end
