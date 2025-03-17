def findPivot(nums):
    # compute prefixes and postfixes
    # where prefix arr index and postfix arr index is same and value is same is pivot
    prefixes = [0]
    for i in range(len(nums) - 1):
        prefixes.append(prefixes[i] + nums[i])

    postfixes = [0]
    for i in range(len(nums) - 1, 0, -1):
        postfixes.insert(0, postfixes[0] + nums[i])

    for i in range(len(prefixes)):
        if prefixes[i] == postfixes[i]:
            return i

    return -1


print(findPivot([2,1,-1]))

