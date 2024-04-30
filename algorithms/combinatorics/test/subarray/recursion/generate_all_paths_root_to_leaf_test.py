import sys

sys.path.append("..")

from algorithms.combinatorics.main.subarray.recursion.generate_all_paths_root_to_leaf import \
    generate_all_paths_root_to_leaf

print(generate_all_paths_root_to_leaf(0, [1, 2, 3], [], []))
