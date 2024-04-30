def generate_repeated_combinations(level, start, nums, path, res):
    # termination condition (LEAF_NODE = nums.length)
    if level == len(nums):
        return []

    for index in range(start, len(nums)):
        # add value to recursion state
        path.append(nums[index])
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))
        # recursion call
        generate_repeated_combinations(level + 1, index, nums, path, res)
        # remove value from recursion state
        path.pop()
    return res
