#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == "]":
                last_str, repeat_count = stack.pop()
                current_str = last_str + current_str * repeat_count
            else:
                current_str += char

        return current_str
# @lc code=end

