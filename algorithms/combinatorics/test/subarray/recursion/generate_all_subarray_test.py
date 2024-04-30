import sys

sys.path.append("..")

from algorithms.combinatorics.main.subarray.recursion.generate_all_subarray import \
    generate_all_subarray

print(generate_all_subarray(0, [1, 2, 3], []))
