
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 1000 and "large" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return None

# print(small_or_large(1000))
# print(small_or_large(1001))
# print(small_or_large(999))
# print(small_or_large(2000))
# print(small_or_large(2001))
# print(small_or_large(1999))

def is_leap_year(year):
    """
        Given a year, return True if it is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# print(is_leap_year(2000))
# print(is_leap_year(2001))
# print(is_leap_year(1900))
# print(is_leap_year(2004))
# print(is_leap_year(2100))
# print(is_leap_year(2400))

def is_leap_year_2(year):
    """
        Given a year, return True if it is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# print(is_leap_year_2(2000))
# print(is_leap_year_2(2001))
# print(is_leap_year_2(1900))
# print(is_leap_year_2(2004))
# print(is_leap_year_2(2100))
# print(is_leap_year_2(2400))

def is_leap_year_3(year):
    """
        Given a year, return True if it is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# print(is_