#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        highest = second_highest = -1
      
        for char in s:
            if char.isdigit():
                value = int(char)
                if value > highest:
                    highest, second_highest = value, highest
                elif second_highest < value < highest:
                    second_highest = value
    
        return second_highest
# @lc code=end

