#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        path_lengths = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_length = max(max_length, path_lengths[depth] + len(name))
            else:
                path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1
        return max_length
# @lc code=end

