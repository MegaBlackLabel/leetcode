#
# @lc app=leetcode id=3200 lang=python3
#
# [3200] Maximum Height of a Triangle
#

# @lc code=start
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calculate_height(c1, c2):
            h = 0
            for i in range(1, 1000):
                if i % 2 == 1:
                    if c1 >= i:
                        c1 -= i
                        h += 1
                    else: 
                        break
                else:
                    if c2 >= i:
                        c2 -= i
                        h += 1
                    else: 
                        break
            return h
        
        return max(calculate_height(red, blue), calculate_height(blue, red))
# @lc code=end

