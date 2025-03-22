#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        nums.sort()
        dp = [1] * len(nums)
        parent = [-1] * len(nums)
        max_len = 1
        max_idx = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
        
        return res
# @lc code=end

