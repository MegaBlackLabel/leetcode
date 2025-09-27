#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        def count(bound: int) -> int:
            ans = 0
            length = 0

            for num in nums:
                if num <= bound:
                    length += 1
                else:
                    length = 0

                ans += length

            return ans

        return count(right) - count(left - 1)
# @lc code=end

