#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        result = []
        
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
                
        return result
# @lc code=end

