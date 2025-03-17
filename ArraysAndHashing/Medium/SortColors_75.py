def sortColors(nums):
    numTwos = 0 # we use this to calculate where to insert 1s
    ptr = 0
    for i in range(len(nums)):
        if nums[ptr] == 0:
            ptr += 1
        elif nums[ptr] == 1:
            nums.insert(len(nums) - numTwos, 1)
            nums.pop(ptr)
        elif nums[ptr] == 2:
            nums.pop(ptr)
            nums.insert(len(nums), 2)
            numTwos += 1

    print(nums)

sortColors([2,0,2,1,1,0])
