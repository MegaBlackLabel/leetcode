#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        result = ''.join(char * count for char, count in sorted_chars)

        return result
# @lc code=end

