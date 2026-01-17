#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_sum_mod = 0
        mod_count = {0: 1}

        for num in nums:
            prefix_sum_mod = (prefix_sum_mod + num) % k
            if prefix_sum_mod < 0:
                prefix_sum_mod += k

            if prefix_sum_mod in mod_count:
                count += mod_count[prefix_sum_mod]
                mod_count[prefix_sum_mod] += 1
            else:
                mod_count[prefix_sum_mod] = 1

        return count
# @lc code=end

