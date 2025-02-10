def maxSubArray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    curr_sum = nums[0] # curr_sum(nums[left_p:right_p+1])
    max_sum = nums[0]
    left_p = 0
    right_p = 1
    while right_p < len(nums):
        if curr_sum < 0:
            left_p = right_p
            right_p += 1
            curr_sum = nums[left_p]
        else:
            curr_sum += nums[right_p]
            right_p += 1

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
