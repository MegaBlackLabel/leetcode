#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
from typing import List


class MagicDictionary:

    def __init__(self):
        
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.prefixes = {}

    def buildDict(self, dictionary: List[str]) -> None:
        
        """
        Build a dictionary through a list of words
        :type dictionary: List[str]
        :rtype: void
        """
        for word in dictionary:
            self.words.add(word)
            for i in range(len(word)):
                prefix = word[:i] + '*' + word[i+1:]
                if prefix not in self.prefixes:
                    self.prefixes[prefix] = set()
                self.prefixes[prefix].add(word)


    def search(self, searchWord: str) -> bool:

        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type searchWord: str
        :rtype: bool
        """
        for i in range(len(searchWord)):
            prefix = searchWord[:i] + '*' + searchWord[i+1:]
            if prefix in self.prefixes:
                for word in self.prefixes[prefix]:
                    if word != searchWord:
                        return True
        return False        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

