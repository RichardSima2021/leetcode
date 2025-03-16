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

def removeDuplicates(nums):
    # slot is where the next unique value would be slotted into
    # we keep going until we find the next unique value, put it in slot, and move the slot up by 1
    # we're not overwriting anything that needs to be preserved
    seen = set()
    uniques = set()
    slot = 0
    for num in nums:
        uniques.add(num)
    k = len(uniques)
    for i in range(len(nums)):
        if slot > k:
            return k

        curr = nums[i]
        if curr not in seen:
            seen.add(curr)
            nums[slot] = curr
            slot += 1

    return k

arr = [0,0,1,1,1,2,2,3,3,4]
# removeDuplicates_bruteForce(arr)
removeDuplicates(arr)
print(arr)