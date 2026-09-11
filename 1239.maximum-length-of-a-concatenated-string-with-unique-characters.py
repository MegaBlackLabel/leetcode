#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [0]
        max_len = 0
        
        for s in arr:
            mask = 0
            is_valid = True
            for char in s:
                bit = 1 << (ord(char) - ord('a'))
                if mask & bit:
                    is_valid = False
                    break
                mask |= bit
            
            if not is_valid:
                continue
                
            for existing_mask in list(dp):
                # If there's no overlap between the characters
                if (existing_mask & mask) == 0:
                    new_mask = existing_mask | mask
                    dp.append(new_mask)
                    max_len = max(max_len, bin(new_mask).count('1'))
                    
        return max_len
# @lc code=end

