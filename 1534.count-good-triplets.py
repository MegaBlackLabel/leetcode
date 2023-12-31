#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(abs(arr[i] - arr[j]) <= a and
               abs(arr[j] - arr[k]) <= b and
               abs(arr[i] - arr[k]) <= c
               for i in range(len(arr))
               for j in range(i + 1, len(arr))
               for k in range(j + 1, len(arr)))
# @lc code=end

