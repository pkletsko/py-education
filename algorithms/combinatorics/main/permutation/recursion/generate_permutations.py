def generate_permutations(ignore_index_set, nums, path, res):
    # termination condition (LEAF_NODE = nums.length)
    if len(ignore_index_set) == len(nums):
        # in compare to dfs implementation where we used global array with default value,
        # here we have to return empty array to cover the case where nums array is empty
        return []

    for index in range(0, len(nums)):
        # pruning
        if index in ignore_index_set:
            continue
        # add value to recursion state
        ignore_index_set.add(index)
        path.append(nums[index])
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))
        # recursion call
        generate_permutations(ignore_index_set, nums, path, res)
        # remove value from recursion state
        path.pop()
        ignore_index_set.remove(index)
    return res
