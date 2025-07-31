#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_str = list(str(num))
        last_index = {int(d): i for i, d in enumerate(num_str)}
        
        for i, d in enumerate(num_str):
            for x in range(9, int(d), -1):
                if x in last_index and last_index[x] > i:
                    num_str[i], num_str[last_index[x]] = num_str[last_index[x]], num_str[i]
                    return int(''.join(num_str))
        
        return num
# @lc code=end

