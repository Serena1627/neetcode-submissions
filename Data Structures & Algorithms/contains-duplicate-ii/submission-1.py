class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {} #num : index
        for i in range(len(nums)):
            if nums[i] in nums_dict and abs(nums_dict[nums[i]] - i) <= k:
                return True
            nums_dict[nums[i]] = i
        return False
        