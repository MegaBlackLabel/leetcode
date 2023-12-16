#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
    
        for a, b in zip(nums[:n], nums[n:]):
            ans.append(a)
            ans.append(b)
        
        return ans
# @lc code=end

