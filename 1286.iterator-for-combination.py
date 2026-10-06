#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def generate_combinations(index: int) -> None:
            """
            Recursively generate all combinations using backtracking.
          
            Args:
                index: Current position in the characters string
            """
            if len(current_combination) == combinationLength:
                all_combinations.append(''.join(current_combination))
                return
          
            if index == string_length:
                return
          
            current_combination.append(characters[index])
            generate_combinations(index + 1)
          
            current_combination.pop()
            generate_combinations(index + 1)
      
        all_combinations = []
        string_length = len(characters)
        current_combination = []
      
        generate_combinations(0)
      
        self.combinations = all_combinations
        self.current_index = 0

    def next(self) -> str:
        result = self.combinations[self.current_index]
        self.current_index += 1
        return result

    def hasNext(self) -> bool:
        return self.current_index < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

