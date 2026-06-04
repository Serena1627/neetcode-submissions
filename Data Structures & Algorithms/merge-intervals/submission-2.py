class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]
        for i in range(len(intervals)):
            current_range = result[-1]
            if current_range[1] >= intervals[i][0]:
                end_point = max(intervals[i][1], current_range[1])
                new_range = [current_range[0], end_point]
                result[-1] = new_range
            else:
                result.append(intervals[i])


        return result
        