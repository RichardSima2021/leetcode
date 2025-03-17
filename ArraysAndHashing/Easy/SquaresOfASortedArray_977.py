def squares(nums):
    squares_p = []
    squares_n = []
    if nums[0] >= 0:
        for num in nums:
            squares_p.append(num ** 2)
        return squares_p

    # starts with negative
    for num in nums:
        if num < 0:
            squares_n.insert(0, num ** 2)
        else:
            squares_p.append(num ** 2)

    # merge two sorted arrays
    res = []
    p1 = 0
    p2 = 0
    while p1 != len(squares_p) and p2 != len(squares_n):
        if squares_p[p1] <= squares_n[p2]:
            res.append(squares_p[p1])
            p1 += 1
        else:
            res.append(squares_n[p2])
            p2 += 1

    if p1 == len(squares_p):
        res += squares_n[p2:]
    else:
        res += squares_p[p1:]

    return res

print(squares([-7,-3,2,3,11]))