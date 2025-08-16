#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        summ = sum(nums)
        if summ % k != 0:
            return False

        target = summ // k 
        if any(num > target for num in nums):
            return False

        def dfs(s: int, remainingGroups: int, currSum: int, used: int) -> bool:
            if remainingGroups == 0:
                return True
            if currSum > target:
                return False
            if currSum == target:
                return dfs(0, remainingGroups - 1, 0, used)

            for i in range(s, len(nums)):
                if used >> i & 1:
                    continue
                if dfs(i + 1, remainingGroups, currSum + nums[i], used | 1 << i):
                    return True

            return False

        nums.sort(reverse=True)
        return dfs(0, k, 0, 0)
# @lc code=end

