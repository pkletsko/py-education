def generate_all_paths_root_to_leaf(start, nums, path, res):
    LEAF_NODE: int = len(nums)
    # termination condition
    if start == LEAF_NODE:
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))

    for index in range(start, LEAF_NODE):
        # add value to recursion state
        path.append(nums[index])
        # recursion call
        generate_all_paths_root_to_leaf(index + 1, nums, path, res)
        # remove value from recursion state
        path.pop()
    return res
