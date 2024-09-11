def twoSum(nums, target):
    numset = set(nums)
    for i in range(len(nums)):
        if target - nums[i] in numset:
            for c in range(len(nums)):
                if c != i and nums[c] == target - nums[i]:
                    return [i, c]
        else:
            continue