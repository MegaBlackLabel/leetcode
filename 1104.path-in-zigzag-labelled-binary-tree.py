#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#

# @lc code=start
import math
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        
        level = int(math.log2(label))
        
        while label >= 1:
            path.append(label)

            level_min = 2 ** level
            level_max = 2 ** (level + 1) - 1
            
            inverted_label = level_max + level_min - label
            
            label = inverted_label // 2
            level -= 1
            
        return path[::-1]
# @lc code=end

