#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sl = SortedList(nums1)

        for i, num in enumerate(nums2):
            index = 0 if sl[-1] <= num else sl.bisect_right(num)
            nums1[i] = sl[index]
            del sl[index]

        return nums1
# @lc code=end

