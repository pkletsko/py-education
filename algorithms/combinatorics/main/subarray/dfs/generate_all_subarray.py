def generate_all_subarray(nums):
    LEAF_NODE: int = len(nums)
    # global result variable
    res = []

    def dfs(start):
        # termination condition
        if start == LEAF_NODE:
            # we don't need to return any value since we collect result to global array
            # if termination happens immediately we will return default value [] (empty array)
            return

        # aggregate variable
        path = []

        for index in range(start, LEAF_NODE):
            # add value to recursion state
            path.append(nums[index])
            # collecting results
            s = [str(i) for i in path]
            res.append("->".join(s))

        dfs(start + 1)

    # start (init recursion call)
    dfs(0)
    return res
