#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#

# @lc code=start
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple) #
        capacity.sort(reverse=True) #

        current_capacity = 0
        boxes_used = 0
        for box_cap in capacity:
            current_capacity += box_cap
            boxes_used += 1
            if current_capacity >= total_apples: #
                return boxes_used
        
        return boxes_used

# @lc code=end

