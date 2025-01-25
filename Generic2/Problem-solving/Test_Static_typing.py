#using static type checking
# In Python 3.6, you declare a variable type like this:
# variable_name: type
# If you are assigning an initial value when you create the variable, it’s as simple as this:
# my_string: str = "My String Value"
# And you declare a function’s input and output types like this:
# def function_name(parameter1: type) -> return_type:

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                    index_map = {}
                    for i in range(len(nums)):
                        num = nums[i]
                        pair = target - num
                        if pair in index_map:
                            return [index_map[pair], i]
                        index_map[num] = i
                    return None
Solution.twoSum("Test",nums=[0,1,6],target=6)
