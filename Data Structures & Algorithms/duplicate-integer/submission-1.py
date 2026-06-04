class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for i in range(len(nums)):
            if nums[i] in distinct:
                return True
            distinct.add(nums[i])
        return False

        