
def fibonacci(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest first value.
    """
    # TODO: Implement me
    pass


# Tests
class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]), 55)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89)]), 89)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144)]), 144)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233)]), 233)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377)]), 377)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377), (15, 610)]), 610)