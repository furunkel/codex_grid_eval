
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The sum of these multiples is 61.
    Return the sum of all the multiples of 2 or 5 below 124.
    """    
    
    sum = 0
    for i in range(1, 125):
        if i % 2 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 5
# Write a function that returns the number of prime numbers that exist up to and including a given integer N.
# For example, count_primes(5) should return 7 because there are seven prime numbers below five.
# Hint: Use a nested for loop to check all numbers from 2 to N
def count_primes(N):
    count = 0
    for i in range(2, N):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 6
# Write a function that checks to see if a number is "happy".
# Return True if happy or False if not.
# The happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and then repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# For example, 5 is unhappy, because it can be expressed as the sum of 1 + 2 + 3 + 4 + 5 = 17.
# Similarly, 200 is unhappy, because it can be expressed as the sum of 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 = 99.
# Write a function that takes in a number and returns True if it is happy, and False if it is unhappy.
def happy(num):
    sum = 0
    while(num != 1):
        sum += num
        num = sum
    return num == 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 7
# Write a function that returns the number of positive integers less than or equal to N.
# For example, count_less_than(9) should return 3 because there are three numbers less than or equal to 9.
def count_less_than(N):
    count = 0
    for i in range(1, N+1):
        if i <= N:
            count += 1
    return count

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 8
# Write a function that checks to see if a number is "happy".
# Return True if happy or False if not.
# The happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and then repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 