def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    min_v = nums[0]
    max_v = nums[0]
    for num in nums:
        if num < min_v:
            min_v = num
        elif num > max_v:
            max_v = num

    l = max_v - min_v
    number_line = ['a'] * (l + 1)

    # print(number_line)

    for num in nums:
        index = num - min_v
        number_line[index] = num

    # print(number_line)

    max_len = 0
    curr_len = 0
    for element in number_line:
        if element == 'a':
            max_len = max(curr_len, max_len)
            curr_len = 0
        else:
            curr_len += 1

    return max(max_len, curr_len)