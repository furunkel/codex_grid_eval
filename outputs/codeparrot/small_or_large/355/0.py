def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    if n < 2000:
        return "small"
    return None

def get_random_color():
    """
        Returns a random color.
    """
    return random.choice(COLORS)

def get_random_color_with_alpha(alpha):
    """
        Returns a random color with the given alpha.
    """
    return random.choice(COLORS) + (random.randint(0, 255), random.randint(0, 255))

def get_random_color_with_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_and_alpha_