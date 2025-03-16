def maxConsecutiveOnes(nums):
    currCum = 0
    maxCum = 0
    for i in nums:
        if i == 1:
            currCum += 1
        else:
            maxCum = max(maxCum, currCum)
            currCum = 0

    return max(maxCum, currCum)
