#
# @lc app=leetcode id=1238 lang=python3
#
# [1238] Circular Permutation in Binary Representation
#

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]

# @lc code=end

