#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
      
        frequency_map = Counter(nums)
      
        for num in sorted(nums):
            if frequency_map[num] > 0:
                for consecutive_num in range(num, num + k):
                    if frequency_map[consecutive_num] == 0:
                        return False
                    frequency_map[consecutive_num] -= 1
      
        return True
# @lc code=end

