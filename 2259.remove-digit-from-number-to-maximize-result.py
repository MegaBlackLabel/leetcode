#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = 0
        for idx, strNum in enumerate(number):
            if strNum == digit:
                newNumber = number[:idx] + number[idx+1:]
                result = max(result, int(newNumber))
        
        return str(result)
# @lc code=end

