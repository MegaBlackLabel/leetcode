#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class TrieNode:
    def __init__(self):
        self.children = [None] * 26 
        self.is_end_of_word = False 


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a') 
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True  

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]
                char_index = ord(char) - ord('a')
                if char == '.':
                    return any(child is not None and dfs(i + 1, child) for child in node.children)
                elif node.children[char_index] is None:
                    return False
                node = node.children[char_index]
            return node.is_end_of_word 

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

