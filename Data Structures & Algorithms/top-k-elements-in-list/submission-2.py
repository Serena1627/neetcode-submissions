class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in range(len(nums)):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1
        max_heap = []
        for key, val in freq_dict.items():
            heapq.heappush(max_heap, (-val, key))
        result = []
        for i in range(k):
            negVal, key = heapq.heappop(max_heap)
            result.append(key)
        return result
            
            
