#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(start: int, path: list[int]) -> None:
            if len(path) == 4 and start == len(s):
                ans.append(path[0] + '.' + path[1] + '.' + path[2] + '.' + path[3])
                return
            if len(path) == 4 or start == len(s):
                return

            for length in range(1, 4):
                if start + length > len(s):
                    return 
                if length > 1 and s[start] == '0':
                    return 
                num = s[start: start + length]
                if int(num) > 255:
                    return
        
                dfs(start + length, path + [num])

        dfs(0, [])
    
        return ans
# @lc code=end

