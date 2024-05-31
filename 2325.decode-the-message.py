#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyToActual = {' ': ' '}
        currChar = 'a'

        for c in key:
            if c not in keyToActual:
                keyToActual[c] = currChar
                currChar = chr(ord(currChar) + 1)

        return ''.join(keyToActual[c] for c in message)
# @lc code=end

