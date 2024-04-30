def generate_all_combinations_or_subsequences(start, nums, path, res):
    # termination condition (LEAF_NODE = nums.length)
    if start == len(nums):
        return []

    for index in range(start, len(nums)):
        # add value to recursion state
        path.append(nums[index])
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))
        # recursion call
        generate_all_combinations_or_subsequences(start + 1, nums, path, res)
        # remove value from recursion state
        path.pop()
    return res
