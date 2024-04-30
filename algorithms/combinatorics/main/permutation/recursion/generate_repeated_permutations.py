def generate_repeated_permutations(level, nums, path, res):
    # termination condition (LEAF_NODE = nums.length)
    if level == len(nums):
        # in compare to dfs implementation where we used global array with default value,
        # here we have to return empty array to cover the case where nums array is empty
        return []

    for index in range(0, len(nums)):
        # add value to recursion state
        path.append(nums[index])
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))
        # recursion call
        generate_repeated_permutations(level + 1, nums, path, res)
        # remove value from recursion state
        path.pop()
    return res
