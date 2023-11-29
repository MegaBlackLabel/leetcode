#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * (len(arr) + 1)

        for a in arr:
            if a <= len(arr):
                count[a] += 1

        for i in range(len(arr), 0, -1):
            if count[i] == i:
                return i

        return -1
    
# @lc code=end

