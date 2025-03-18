def rotate(nums, k):
    # can only rotate max of len(nums) which goes back to original
    # bijection from old to new
    # 1, 2, 3, 4 rotate 2
    # 0 -> 2 = (0 + 2) % 4
    # 1 -> 3 = (1 + 2) % 4
    # 2 -> 0 = (2 + 2) % 4
    # 3 -> 1 = (3 + 2) % 4

    # 1, 2, 3, 4 rotate 3
    # 0 -> 3 = (0 + 3) % 4
    # 1 -> 0 = (1 + 3) % 4
    # 2 -> 1 = (2 + 3) % 4
    # 3 -> 2 = (3 + 3) % 4

    # generate hash map
    # 0 goes to 3 then find what 3 goes to

    index_map = dict()
    nums_len = len(nums)

    steps = k % nums_len

    for i in range(nums_len):
        index_map[i] = (i + steps) % nums_len

    print(index_map)

    if steps == nums_len / 2:
        for i in range(steps):
            nums[i], nums[int(i + (nums_len) / 2)] = nums[int(i + (nums_len) / 2)], nums[i]
    else:
        # start at 0
        curr_idx = 0
        save = nums[curr_idx]
        for i in range(len(index_map.keys())):
            next_idx = index_map[curr_idx]
            # swap
            save, nums[next_idx] = nums[next_idx], save
            curr_idx = next_idx
            print(f'Nums: {nums}, saved: {save}')


arr = [1,2,3,4,5,6]
rotate(arr, 2)
print(arr)








