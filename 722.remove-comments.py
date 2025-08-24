#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        in_block = False
        result = []
        new_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if line[i:i + 2] == '*/':
                        in_block = False
                        i += 1
                else:
                    if line[i:i + 2] == '/*':
                        in_block = True
                        i += 1
                    elif line[i:i + 2] == '//':
                        break
                    else:
                        new_line.append(line[i])
                i += 1

            if not in_block and new_line:
                result.append(''.join(new_line))
                new_line = []

        return result
# @lc code=end

