
def some_func(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
    return max(text, key=lambda x: x[-1])[-1]

print(some_func([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

# Output: 5

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(num):
    """
    Given a number, return the factorial of that number.
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(8))

# Output: 40320

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def some_func(num):
    """
    Given a number, return a dictionary with the key being the number and the value being the square of that number.
    """
    return {x: x * x for x in range(1, num + 1)}

print(some_func(8))

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '