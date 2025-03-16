def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    i = 0
    while True:
        print(intervals)
        if i == len(intervals) - 1:
            return intervals
        if intervals[i][1] >= intervals[i+1][0]:
            # merge these two intervals
            new_interval = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
            intervals.pop(i)
            intervals.pop(i)
            intervals.insert(i, new_interval)
        else:
            i += 1




print(merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))