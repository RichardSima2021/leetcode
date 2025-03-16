def runningSum(nums):
    sum = 0
    running = []
    for num in nums:
        sum += num
        running.append(sum)

    return running