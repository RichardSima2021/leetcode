def majorityElement(nums):
    nums = sorted(nums)
    return nums[len(nums) // 2]
