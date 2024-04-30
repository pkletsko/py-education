import sys

sys.path.append("..")

from algorithms.combinatorics.main.subarray.dfs.generate_all_paths_root_to_leaf import \
    generate_all_paths_root_to_leaf

print(generate_all_paths_root_to_leaf([1, 2, 3]))
