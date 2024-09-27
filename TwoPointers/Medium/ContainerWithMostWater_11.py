def ContainerMostWaterBruteForce(height):
    # brute force method: check every single possible combination of heights
    max_vol = 0

    for i in range(len(height)):
        for c in range(1,len(height)):
            height_l = height[i]
            height_r = height[c]
            length = c - i
            volume = min(height_l, height_r) * length
            if volume > max_vol:
                max_vol = volume

    return max_vol

def ContainerMostWaterOptimal(height):
    left = 0
    right = len(height) - 1

    max_volume = 0
    while left < right:
        left_height = height[left]
        right_height = height[right]
        volume = min(left_height, right_height) * (right - left)

        if volume > max_volume:
            max_volume = volume
        if left_height < right_height:
            left += 1
        else:
            right -= 1

    return max_volume


# print(ContainerMostWaterBruteForce([1,8,6,2,5,4,8,3,7]))
print(ContainerMostWaterOptimal([1,8,6,2,5,4,8,3,7]))