#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()

        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                return True
            else:
                hashmap[nums[i]] = i

        return False


# @lc code=end
