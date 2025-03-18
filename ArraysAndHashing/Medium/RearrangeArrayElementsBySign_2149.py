def rearrangeArray(nums):
    positives = []
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    res = []
    for i in range(len(positives)):
        res.append(positives[i])
        res.append(negatives[i])

    return res

print(rearrangeArray([3,1,-2,-5,2,-4]))