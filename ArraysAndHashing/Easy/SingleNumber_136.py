def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    val = nums[0]
    for num in nums[1:]:
        val = val ^ num

    return val