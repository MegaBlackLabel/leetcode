#
# @lc app=leetcode id=1138 lang=python3
#
# [1138] Alphabet Board Path
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        curr_r, curr_c = 0, 0
        path = []
        
        for char in target:
            ascii_offset = ord(char) - ord('a')
            target_r = ascii_offset // 5
            target_c = ascii_offset % 5
            
           
            if target_c < curr_c:
                path.append('L' * (curr_c - target_c))
            if target_r < curr_r:
                path.append('U' * (curr_r - target_r))
            if target_c > curr_c:
                path.append('R' * (target_c - curr_c))
            if target_r > curr_r:
                path.append('D' * (target_r - curr_r))
                
            path.append('!')
            
            curr_r, curr_c = target_r, target_c
            
        return "".join(path)
# @lc code=end

