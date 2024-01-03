#
# @lc app=leetcode id=1566 lang=python3
#
# [1566] Detect Pattern of Length M Repeated K or More Times
#

# @lc code=start
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = 0
        
        for i in range(m, len(arr)):
            count = count + 1 if arr[i] == arr[i - m] else 0
            if count == m * k - m:
                return True
        
        return False
# @lc code=end

