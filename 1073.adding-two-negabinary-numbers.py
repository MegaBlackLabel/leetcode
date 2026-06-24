#
# @lc app=leetcode id=1073 lang=python3
#
# [1073] Adding Two Negabinary Numbers
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        carry = 0
        i, j = len(arr1) - 1, len(arr2) - 1
    
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += arr1[i]
                i -= 1
            if j >= 0:
                carry += arr2[j]
                j -= 1
                

            ans.append(carry & 1)
            carry = -(carry >> 1)
            
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
            
        return ans[::-1]
# @lc code=end

