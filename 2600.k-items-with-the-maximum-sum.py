#
# @lc app=leetcode id=2600 lang=python3
#
# [2600] K Items With the Maximum Sum
#

# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
    
        if k <= numOnes + numZeros:
            return numOnes
    
        return numOnes - (k - numOnes - numZeros)
# @lc code=end

