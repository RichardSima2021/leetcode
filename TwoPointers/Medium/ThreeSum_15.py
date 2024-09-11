def threeSum(nums):
    # a + b + c == 0
    # b + c == 0 - a
    triplets = set()
    def twoSum(target, sub_nums):
        valid_pairs = set()
        for j in range(len(sub_nums)):
            num_1 = sub_nums[j]
            if target - num_1 in set(sub_nums[0:j] + sub_nums[j+1:]):
                valid_pairs.add(tuple(sorted([num_1, target - num_1])))
        return valid_pairs

    for i in range(len(nums)):
        a = nums[i]
        valid_pairs = twoSum(0 - nums[i], nums[0:i] + nums[i+1:])
        for pair in valid_pairs:
            b,c = pair
            triplets.add(tuple(sorted([a,b,c])))

    triplet_list = []
    for triplet in triplets:
        triplet_list.append(list(triplet))

    return triplet_list

print(threeSum([-1,0,1,2,-1,-4]))

