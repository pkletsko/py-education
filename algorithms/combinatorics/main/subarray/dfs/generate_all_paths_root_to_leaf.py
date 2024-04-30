def generate_all_paths_root_to_leaf(nums):
    LEAF_NODE: int = len(nums)
    # global result variable
    res = []

    def dfs(start, path):
        # termination condition
        if start == LEAF_NODE:
            # collecting results
            s = [str(i) for i in path]
            res.append("->".join(s))

        for index in range(start, LEAF_NODE):
            # add value to recursion state
            path.append(nums[index])
            # recursion call
            dfs(index + 1, path)
            # remove value from recursion state
            path.pop()

    # start (init recursion call)
    dfs(0, [])
    return res
