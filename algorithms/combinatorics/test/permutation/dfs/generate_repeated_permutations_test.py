import sys

sys.path.append("..")

from algorithms.combinatorics.main.permutation.dfs.generate_repeated_permutations import \
    generate_repeated_permutations

print(generate_repeated_permutations([1, 2, 3]))
