#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
import collections
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = collections.Counter()
        for nums in nums1, nums2, nums3:
            count.update(set(nums))
        
        return [i for i, c in count.items() if c >= 2]
# @lc code=end

