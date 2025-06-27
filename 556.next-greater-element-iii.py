#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        digits = list(str(n))
        length = len(digits)

        pivot = length - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1

        if pivot == -1:
            return -1
        
        successor = length - 1
        while successor > pivot and digits[successor] <= digits[pivot]:
            successor -= 1      

        digits[pivot], digits[successor] = digits[successor], digits[pivot]

        digits = digits[:pivot + 1] + digits[pivot + 1:][::-1]
        result = int(''.join(digits))
        return result if result < 2**31 else -1
    
# @lc code=end

