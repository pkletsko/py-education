def generate_all_combinations_or_sub_sequences(nums):
    LEAF_NODE: int = len(nums)
    # global result variable
    res = []

    def dfs(start, path):
        # termination condition
        if start == LEAF_NODE:
            # we don't need to return any value since we collect result to global array
            # if termination happens immediately we will return default value [] (empty array)
            return
        for index in range(start, LEAF_NODE):
            # add value to recursion state
            path.append(nums[index])
            # collecting results
            s = [str(i) for i in path]
            res.append("->".join(s))
            # recursion call
            dfs(index + 1, path)
            # remove value from recursion state
            path.pop()
    # start (init recursion call)
    dfs(0, [])
    return res
