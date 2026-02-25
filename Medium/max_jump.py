def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False  # can't reach this point
        max_reach = max(max_reach, i + nums[i])

    return True