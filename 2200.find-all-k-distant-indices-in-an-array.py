#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []

        j = 0
        for i in range(n):
            while j < n and (nums[j] != key or j < i - k):
                j += 1
            if j == n:
                break
            if abs(i - j) <= k:
                ans.append(i)

        return ans
# @lc code=end

