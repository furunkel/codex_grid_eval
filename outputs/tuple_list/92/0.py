
def f(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[1]

print(f([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

# Output: 5

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input())
print(fact(x))

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input())
d = dict()

for i in range(1, n + 1):
    d[i] = i * i

print(d)

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

values = input()
l = values.split(",")
t = tuple(l)
print(l)
print(t)

# ----------------------------------------------------------------------------------------------------------------------

# Question:
# Define a class which has at least two methods:
# getString: to