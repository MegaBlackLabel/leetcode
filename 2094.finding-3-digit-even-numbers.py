#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
import collections
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        count = collections.Counter(digits)

        for a in range(1, 10):
            for b in range(0, 10):
                for c in range(0, 9, 2):
                    if count[a] > 0 and count[b] > (b == a) and count[c] > (c == a) + (c == b):
                        ans.append(a * 100 + b * 10 + c)

        return ans
    
# @lc code=end

