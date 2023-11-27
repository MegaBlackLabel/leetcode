#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0

        arr2.sort()

        for a in arr1:
            i = bisect.bisect_left(arr2, a)
            if (i == len(arr2) or arr2[i] - a > d) and (i == 0 or a - arr2[i - 1] > d):
                ans += 1

        return ans
# @lc code=end

