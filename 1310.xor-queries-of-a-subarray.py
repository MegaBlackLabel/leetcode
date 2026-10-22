#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
from itertools import accumulate


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix_xor = list(accumulate(arr, xor, initial=0))
      
        result = []
        for left, right in queries:
            subarray_xor = prefix_xor[right + 1] ^ prefix_xor[left]
            result.append(subarray_xor)
      
        return result
# @lc code=end

