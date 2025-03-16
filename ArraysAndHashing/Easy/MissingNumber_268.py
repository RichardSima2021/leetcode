def missingNumber_nlogn(nums):
    nums.sort()
    if nums[0] != 0:
        return 0
    if nums[-1] != len(nums):
        return len(nums)
    counter = 0
    for num in nums:
        if num != counter:
            return counter
        counter += 1
    return -1

def missingNumber(nums):
    # nums from 0 to n one missing
    # not sorted order
    # log n means can't sort
    # iterate 2 or 3 times?
    # sum expected minus actual sum = missing number
    expectedSum = 0
    for i in range(len(nums) + 1):
        expectedSum += i

    actualSum = 0
    for i in nums:
        actualSum += i

    return expectedSum - actualSum