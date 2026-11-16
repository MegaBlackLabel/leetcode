#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#

# @lc code=start
from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        frequency_counter = Counter(arr)
      
        min_set_size = 0
        removed_count = 0
      
        for element, frequency in frequency_counter.most_common():
            removed_count += frequency
            min_set_size += 1
            
            if removed_count * 2 >= len(arr):
                break
      
        return min_set_size
# @lc code=end

