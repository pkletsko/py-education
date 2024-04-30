def generate_permutations(nums):
    LEAF_NODE: int = len(nums)
    # global result variable
    res = []

    def dfs(ignore_index_set, path):
        # termination condition
        if len(ignore_index_set) == LEAF_NODE:
            # we don't need to return any value since we collect result to global array
            # if termination happens immediately we will return default value [] (empty array)
            return
        for index in range(0, LEAF_NODE):
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
            dfs(ignore_index_set, path)
            # remove value from recursion state
            path.pop()
            ignore_index_set.remove(index)

    # start (init recursion call)
    dfs(set(), [])
    return res
