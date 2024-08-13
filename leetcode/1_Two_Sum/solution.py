import unittest
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff in memo:
                return [i, memo[diff]]
            else:
                memo.update({nums[i]: i})


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        self.assertEqual(solution.two_sum([2, 7, 11, 15], 9), [1, 0])


if __name__ == '__main__':
    unittest.main()
