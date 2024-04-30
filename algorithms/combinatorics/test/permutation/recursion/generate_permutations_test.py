import sys

sys.path.append("..")

from algorithms.combinatorics.main.permutation.recursion.generate_permutations import \
    generate_permutations

print(generate_permutations(set(), [1, 2, 3], [], []))