
def fibonacci(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    # TODO: Implement me
    pass


# Tests
class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci([(1, 1), (2, 1), (1, 2), (1, 3), (2, 1), (1, 4), (1, 5), (2, 4)]), 1)
        self.assertEqual(fibonacci([(1, 2), (1, 1), (2, 2), (1, 3), (1, 4), (2, 3), (1, 5), (2, 5), (1, 6)]), 1)
        self.assertEqual(fibonacci([(1, 1), (2, 2), (1, 3), (2, 3), (1, 4), (2, 5), (1, 5), (1, 6), (2, 8)]), 1)
        self.assertEqual(fibonacci([(1, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (1, 7), (2, 8), (1, 9)]), 1)
        self.assertEqual(fibonacci([(2, 1), (1, 1), (2, 2), (1, 3), (2, 3), (1, 4), (2, 5), (1, 5), (1, 6)]), 1)
        self.assertEqual(fibonacci([(2, 1), (1, 2), (1, 1), (2, 2), (1, 3), (2, 3), (1, 4), (2, 5), (1, 5)]), 1)
        self.assertEqual(fibonacci([(2, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 4), (2, 5), (1, 5), (1, 6)]), 1)
        self.assertEqual(fibonacci([(2, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 4), (2, 5), (