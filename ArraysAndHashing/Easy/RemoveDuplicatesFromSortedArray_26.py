def removeDuplicates_bruteForce(nums):
    unique_vals = set()
    for num in nums:
        unique_vals.add(num)

    k = len(unique_vals)

    seen = set()
    i = 0
    while i < k:
        print(i)
        cur = nums[i]
        if cur in seen:
            # move to end
            # achieves this but in place
            # nums = nums[0:i] + nums[i+1:] + nums[i:i+1]
            for c in range(i, len(nums)-1):
                nums[c], nums[c+1] = nums[c+1], nums[c]
        else:
            i += 1
            seen.add(cur)

        print(nums)


    return k

arr = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates_bruteForce(arr)
print(arr)