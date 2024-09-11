def productExceptSelf(nums):
    prefixes = [0] * len(nums)
    prefixes[0] = 1
    postfixes = [0] * len(nums)
    postfixes[-1] = 1
    # compute prefixes and postfixes
    # prefix[i] = all numbers multiplied before i
    # postfix[i] = all numbers multiplied after i

    # original  [1,  2,  3,  4]
    # prefix    [1,  1,  2,  6]
    # postfix   [24, 12, 4,  1]

    # final =   [24, 12, 8,  6]
    prod = 1
    for i in range(1, len(nums)):
        prod *= nums[i - 1]
        prefixes[i] = prod

    prod = 1
    for i in range(len(nums) - 2, -1, -1):
        prod *= nums[i + 1]
        postfixes[i] = prod

    res = []
    for i in range(len(prefixes)):
        res.append(prefixes[i] * postfixes[i])

    return res
