def check(nums: List[int]) -> bool:
    # 0 value drops: array is sorted
    # 1 value drop: array is sorted and rotated - the value at the drop must be largest value seen
    # 2+ value drops: array is not sorted and rotated
    num_drops = 0
    drop_idx = -1
    cur = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < cur:
            num_drops += 1
            drop_idx = i

        cur = nums[i]

        if num_drops == 2:
            return False
    if num_drops == 0:
        return True

    return (nums[drop_idx:] + nums[0:drop_idx]) == sorted(nums)