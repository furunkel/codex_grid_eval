
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]

print(f([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

# 2.
def f(text):
    """
    Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
    """
    return sorted(text, key=lambda x: x[-1])

print(f([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 3.
def f(text):
    """
    Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
    """
    import random
    while True:
        x = random.randint(0, n-1)
        if x not in l:
            return x

print(f(10, [1, 3, 5, 6, 7]))

# 4.
def f(text):
    """
    Given a list of words, return a list of words with duplicates removed.
    """
    return list(set(text))

print(f(['a', 'b', 'b', 'c', 'a']))

# 5.
def f(text):
    """
    Given two sorted lists, return a list of the elements in sorted order.
    """
    return sorted(text[0] + text[1])

print(f([[1, 3, 5], [2, 6, 8]]))

# 6.
def f(text):
    """
    Given a list of words, return a list of the lengths of each word.
    """
    return [len(x) for x in text]

print(f(['hello', 'world']))

# 7.
def f(text):
    """
    Given a list of words, return a list of words with the vowels removed.
    """
    return [x.replace('a', '').replace('e', '').replace('i', '').replace('o', '').