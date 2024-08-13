import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        PRICES_SIZE: int = len(prices)
        if PRICES_SIZE < 2:
            return 0

        maxProfit = 0

        minSoFar = prices[0]

        for index in range(1, PRICES_SIZE):
            if prices[index] > minSoFar:
                maxProfit = max(maxProfit, prices[index] - minSoFar)
            else:
                minSoFar = prices[index]
        return maxProfit


class TestSolution(unittest.TestCase):
    def test_max_profit(self):
        solution = Solution()
        # Test case 1: Example input [7,1,5,3,6,4]
        self.assertEqual(solution.max_profit([7, 1, 5, 3, 6, 4]), 5)
        # Test case 2: Example input [7,6,4,3,1]
        self.assertEqual(solution.max_profit([7, 6, 4, 3, 1]), 0)
        # Test case 3: Empty input
        self.assertEqual(solution.max_profit([]), 0)
        # Test case 4: Single element input
        self.assertEqual(solution.max_profit([5]), 0)
        # Test case 5: All increasing prices
        self.assertEqual(solution.max_profit([1, 2, 3, 4, 5]), 4)
        # Test case 6: All decreasing prices
        self.assertEqual(solution.max_profit([5, 4, 3, 2, 1]), 0)


if __name__ == '__main__':
    unittest.main()