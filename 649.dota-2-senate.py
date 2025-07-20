#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant = []
        dire = []
        
        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.pop(0) + len(senate))
                dire.pop(0)
            else:
                dire.append(dire.pop(0) + len(senate))
                radiant.pop(0)
        
        return "Radiant" if radiant else "Dire"
# @lc code=end

