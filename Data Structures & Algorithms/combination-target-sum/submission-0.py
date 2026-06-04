class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(curr_sum_list, curr_sum, remaining_nums):
            if not remaining_nums:
                return
            #adding the current number and it becomes more than the target
            #adding the current number and it is less than the target
            #not adding the current number
            for i in range(len(remaining_nums)):
                num_to_add = remaining_nums[i]
                curr_sum_list.append(num_to_add)
                curr_sum += num_to_add
                if curr_sum > target:
                    curr_sum_list.pop()
                    curr_sum -= num_to_add
                    continue
                if curr_sum == target:
                    result.append(curr_sum_list[:])
                new_rem = remaining_nums[i:]
                dfs(curr_sum_list, curr_sum, new_rem)
                curr_sum_list.pop()
                curr_sum -= num_to_add
        
        dfs([],0,nums)
        return result
            
        