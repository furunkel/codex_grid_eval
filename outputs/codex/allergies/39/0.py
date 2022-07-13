
def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

    An allergy test produces a single numeric score which contains the
    information about all the allergies the person has (that they were
    tested for).

    The list of items (and their value) that were tested are:

    * eggs (1)
    * tomatoes (2)
    * peanuts (4)
    * pollen (8)
    * strawberries (16)
    * cats (32)
    * chocolate (64)
    * shellfish (128)

    So if Alice is allergic to chocolate and shellfish, he gets a score of 192.

    Now, given just that score of 192, your program should return a list of all the allergens Alice is allergic to.

    Note: a given score may include allergens **not** listed above (i.e.
    allergens that score 256, 512, 1024, etc.).  Your program should
    ignore those components of the score.  For example, if the allergy
    score is 257, your program should only report the eggs (1) allergy.
    """
    allergens = {
        1: 'eggs',
        2: 'tomatoes',
        4: 'peanuts',
        8: 'pollen',
        16: 'strawberries',
        32: 'cats',
        64: 'chocolate',
        128: 'shellfish'
    }

    return [allergens[allergen] for allergen in allergens if score & allergen]


def is_triangle(a, b, c):
    """
    Given the lengths of three sides of a triangle, return whether the triangle is a right triangle.

    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(4, 3, 5)
    True
    >>> is_triangle(5, 3, 4)
    True
    >>> is_triangle(10, 10, 10)
    False
    """
    return (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)


def is_isogram(word):
    """
    Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.

    Examples of isograms:

    >>> is_isogram("Dermatoglyphics")
    True
    >>> is_isogram("aba")
    False
    >>> is_isogram("moOse")
    False
    """
    return len(word) == len(set(word.lower()))


def is_prime(number):
    """
    Determine if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(9)
    False
    """
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primes(count):
    """
    Return a list of the first count prime numbers.

