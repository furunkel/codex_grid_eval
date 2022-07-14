def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "house" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n < 2000:
        return "house"
    else:
        return "large"


def get_random_number(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_number_between(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_number_between_two_numbers(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_number_between_two_numbers_and_three_numbers(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value), random.randint(min_value, max_value)


def get_random_number_between_two_numbers_and_three_numbers_and_four_numbers(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value), random.randint(min_value, max_value), random.randint(min_value, max_value)


def get_random_number_between_two_numbers_and_four_numbers_and_five_numbers(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value), random.randint(min_value, max_value), random.randint(min_value, max_value), random.randint(min_value, max_value)


def get_random_number_between_two_numbers_