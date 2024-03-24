#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[k - 1] - nums[0]

        for i in range(k, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])

        return ans
    
# @lc code=end

