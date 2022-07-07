
def fibonacci(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    # TODO: Implement me
    pass


# Tests
class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]),
                         10)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55),
                                    (11, 89), (12, 144), (13, 233), (14, 377), (15, 610), (16, 987), (17, 1597),
                                    (18, 2584), (19, 4181), (20, 6765)]), 20)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55),
                                    (11, 89), (12, 144), (13, 233), (14, 377), (15, 610), (16, 987), (17, 1597),
                                    (18, 2584), (19, 4181), (20, 6765), (21, 10946), (22, 17711), (23, 28657),
                                    (24, 46368), (25, 75025), (26, 121393), (27, 196418), (28, 317811), (29, 514229),
                                    (30, 832040)]), 30)
        self.assertEqual(fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55),
                                    (11, 89), (12, 144), (13,