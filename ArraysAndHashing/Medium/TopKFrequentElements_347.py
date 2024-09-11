def topKFrequent(nums, k):
    num_counts = dict()
    # map num to count
    for i in nums:
        if i not in num_counts.keys():
            num_counts[i] = 0
        num_counts[i] += 1

    # sort by count
    k_frequent_items = sorted(num_counts.items(), key=lambda x: x[1], reverse=True)

    k_frequent_nums = []

    for item in k_frequent_items[:k]:
        k_frequent_nums.append(item[0])

    return k_frequent_nums