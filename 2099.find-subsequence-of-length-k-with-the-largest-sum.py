#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        threshold = sorted(nums)[-k]
        larger = sum(num > threshold for num in nums)
        equal = k - larger

        for num in nums:
            if num > threshold:
                ans.append(num)
            elif num == threshold and equal:
                ans.append(num)
                equal -= 1

        return ans
# @lc code=end

