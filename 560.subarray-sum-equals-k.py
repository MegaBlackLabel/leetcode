#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        Returns the number of continuous subarrays whose sum equals to k.
        Uses a hashmap to store the cumulative sum and its frequency.
        """
        count = 0
        cumulative_sum = 0
        sum_map = {0: 1}
        for num in nums:
            cumulative_sum += num
            
            if cumulative_sum - k in sum_map:
                count += sum_map[cumulative_sum - k]
            
            if cumulative_sum in sum_map:
                sum_map[cumulative_sum] += 1
            else:
                sum_map[cumulative_sum] = 1
        return count
# @lc test=1
# @lc code=end

