#
# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        file_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                file_map[content].append(f"{directory}/{file_name}")
                
        return [files for files in file_map.values() if len(files) > 1]
# @lc code=end

