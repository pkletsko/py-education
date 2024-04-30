def generate_all_subarray(start, nums, res):
    LEAF_NODE: int = len(nums)

    # termination condition
    if start == LEAF_NODE:
        # we don't need to return any value since we collect result to global array
        # if termination happens immediately we will return default value [] (empty array)
        return []

    # aggregate variable
    path = []

    for index in range(start, LEAF_NODE):
        # add value to recursion state
        path.append(nums[index])
        # collecting results
        s = [str(i) for i in path]
        res.append("->".join(s))

    # start (init recursion call)
    generate_all_subarray(start + 1, nums, res)
    return res
