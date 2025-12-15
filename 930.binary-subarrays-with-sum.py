#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = {0: 1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            if current_sum - goal in count:
                result += count[current_sum - goal]
            count[current_sum] = count.get(current_sum, 0) + 1

        return result
# @lc code=end

