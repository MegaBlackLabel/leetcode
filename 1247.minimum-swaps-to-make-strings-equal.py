#
# @lc app=leetcode id=1247 lang=python3
#
# [1247] Minimum Swaps to Make Strings Equal
#

# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0
        
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy_count += 1
            elif c1 == 'y' and c2 == 'x':
                yx_count += 1
                
        if (xy_count + yx_count) % 2 != 0:
            return -1
            
        swaps = (xy_count // 2) + (yx_count // 2)
        
        if xy_count % 2 != 0:
            swaps += 2
            
        return swaps
# @lc code=end

