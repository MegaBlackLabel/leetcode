#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations_count = 0
        for num in nums:
            # Check the remainder when divided by 3
            remainder = num % 3
            if remainder != 0:
                # If the remainder is 1 (e.g., 4), subtract 1.
                # If the remainder is 2 (e.g., 5), add 1.
                # In both cases, only 1 operation is needed.
                operations_count += 1
        return operations_count
# @lc code=end

