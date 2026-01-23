#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for val, index in queries:
            original_value = nums[index]

            if original_value % 2 == 0:
                even_sum -= original_value

            nums[index] += val
            new_value = nums[index]

            if new_value % 2 == 0:
                even_sum += new_value

            result.append(even_sum)

        return result
# @lc code=end

