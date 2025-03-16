def moveZeros(nums):
    ptr = 0
    for i in range(len(nums)):
        if nums[ptr] == 0:
            # move to back
            nums.pop(ptr)
            nums.append(0)
        else:
            ptr += 1
    print(nums)

moveZeros([0,1,0,3,12])
