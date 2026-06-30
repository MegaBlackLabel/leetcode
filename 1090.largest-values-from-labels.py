#
# @lc app=leetcode id=1090 lang=python3
#
# [1090] Largest Values From Labels
#

# @lc code=start
from typing import Counter, List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        
        total_sum = 0
        items_selected = 0
        label_counts = Counter()
        
        for value, label in items:
            if label_counts[label] < useLimit:
                label_counts[label] += 1
                total_sum += value
                items_selected += 1
                
                if items_selected == numWanted:
                    break
                    
        return total_sum
# @lc code=end

