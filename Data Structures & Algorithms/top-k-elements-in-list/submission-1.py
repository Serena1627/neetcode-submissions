import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Explore
        #The idea is to return the n most frequent elements in the array
        #CQ- can more than one element have the same frequency, what do you do if the nums is empty or none?

        #Brainstorm
        #FI-make a frequency dictionary. 
        #Plan
        #Implement
        #Verify
        if not nums:
            return []

        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        '''
        min_heap = []
        for num, frequency in frequencies.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (frequency, num))
            else:
                if frequency > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (frequency, num))

        return [num for (frequency, num) in min_heap]
        '''
        buckets = [[] for x in range(len(nums)+1)]
        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        
        return result

            







        