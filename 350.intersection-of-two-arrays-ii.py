#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        ans = []
        count = collections.Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1

        return ans


# @lc code=end
