class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Explore
        #The idea is to find the additive pair for the target and return their indexes
        #CQ- can the target be 0 or 1? is the list sorted?
        #Brainstorm
        #FI-make a dictionary with the additive inverse of each number for i
        #loop through j and try to find which i-index has the additive index as a value in the dictionary
        #SI- Use 2 pointers. If left+right < target increment the left pointer, if left + right > target decrement the right pointer
        #until you get 2 that add up to the target
        #Plan
        #Implement
        my_dict = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in my_dict:
                left = my_dict[complement] if my_dict[complement] < i else i
                right = my_dict[complement] if my_dict[complement] > i else i
                return [left, right]
            my_dict[nums[i]] = i
        
        #Verify
        