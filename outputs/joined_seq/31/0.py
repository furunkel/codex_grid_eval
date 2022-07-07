
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with two underscores and True otherwise.
    """
    return re.search(r'[a-z]{2}__[a-z]{2}', text) is None

def match_ends(words):
    """
    Write a function that takes a list of strings and returns the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
    """
    return len([word for word in words if len(word) >= 2 and word[0] == word[-1]])

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
    """
    x_words = [word for word in words if word[0] == 'x']
    other_words = [word for word in words if word[0] != 'x']
    return sorted(x_words) + sorted(other_words)

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
    """
    return sorted(tuples, key=lambda t: t[-1])

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3].
    """
    return [num for i, num in enumerate(nums) if i == 0 or num != nums[i - 1]]

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order.
    """
    return sorted(list1 + list2)

def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']