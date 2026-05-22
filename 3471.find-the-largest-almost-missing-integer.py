#
# @lc app=leetcode id=3471 lang=python3
#
# [3471] Find the Largest Almost Missing Integer
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n: 
            return max(nums)
        
        count = Counter(nums)
        
        candidates = []
        if k == 1:
            candidates = [num for num, freq in count.items() if freq == 1]
        else:
            if count[nums[0]] == 1: 
                candidates.append(nums[0])
            if count[nums[-1]] == 1: 
                candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1

# @lc code=end

