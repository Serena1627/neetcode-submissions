class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        final = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
            else:
                final.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]

        final.append([left, right])
        return final
            
        