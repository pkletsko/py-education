import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Set initial minimum price to a large number
        max_profit = 0  # No profit initially

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price found so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Calculate new max profit if current price provides a better profit

        return max_profit


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
