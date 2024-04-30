import sys

sys.path.append("..")

from algorithms.combinatorics.main.combination_subsequence.recursion.generate_repeated_combinations import \
    generate_repeated_combinations

print(generate_repeated_combinations(0, 0, [1, 2, 5], [], []))
