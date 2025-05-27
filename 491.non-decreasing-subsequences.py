#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, path):
            if len(path) > 1:
                res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        res = []
        backtrack(0, [])
        return res
# @lc code=end

