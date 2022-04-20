
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

    So if Tom is allergic to chocolate and pollen, he gets a score of 72.

    Now, given just that score of 72, your program should return a list of all the allergens Tom is allergic to.

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


def is_prime(number):
    """
    Return True if *number* is prime.
    """
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


def primes(count):
    """
    Return a list of *count* prime numbers.
    """
    primes = []
    number = 2

    while len(primes) < count:
        if is_prime(number):
            primes.append(number)
        number += 1

    return primes


def sort_by_length(words):
    """
    Given list of words, return list of ascending [(len, [words])].
    Given ["I", "like", "apples", "bananas", "you"],
    return [(1, ['I']), (3, ['you']),
            (4, ['like']), (5, ['apples']),
            (6, ['bananas'])].
    """
    words_by_length = {}

    for word in words:
        words_by_length.setdefault(len(word), []).append(word)

    return sorted(words_by_length.items())


def translate(phrase):
    """
    Translate phrase to pig latin.
    Given "shmanthony is the best teacher", return "Anthonyshmay isay ethay estbay eachertay".
    """
    translation = ""
    for word in phrase.split():
        translation += word[1:] + word[0] + "ay "
    return translation.strip()


def valid_parentheses(string):
    """
    Given a string containing just the characters '(', ')', '{',