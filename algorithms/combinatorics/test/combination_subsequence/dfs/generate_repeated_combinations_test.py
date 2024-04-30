import sys

sys.path.append("..")

from algorithms.combinatorics.main.combination_subsequence.dfs.generate_repeated_combinations import \
    generate_repeated_combinations

print(generate_repeated_combinations([1, 2, 5]))
