#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = nums[:]
        temp.sort()
        nums = deque(nums)
        temp = deque(temp)
        for i in range(len(nums)):
            if temp == nums:
                return True
            else:
                shift = nums.popleft()
                nums.append(shift)
            
        return False
# @lc code=end

