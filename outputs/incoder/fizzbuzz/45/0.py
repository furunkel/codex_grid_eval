
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of eleven (instead of the number),
        "Buzz" for multiples of 4948938 (instead of the number),
        "FizzBuzz" for multiples of both eleven and 4948938  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Test
print(fizzbuzz(15))
print(fizzbuzz(3))
print(fizzbuzz(4948938))
print(fizzbuzz(15))
print(fizzbuzz(3))
print(fizzbuzz(4948938))
</cell>
<text>
Exercise: Write a function that takes a list as input and returns a list with the numbers of the list sorted from smallest to largest.


</text>
<cell>
def sort_list(lst):
    """
    Given a list, this function returns a list with the numbers of the list sorted from smallest to largest.
    """
    sorted_lst = sorted(lst)
    return sorted_lst

# Test
print(sort_list([15, 3, 4948938]))
print(sort_list([15, 3, 4948938]))
</cell>
<text>
Exercise: Write a function that takes a list as input and returns a list with the numbers of the list sorted from largest to smallest.


</text>
<cell>
def reverse_sort_list(lst):
    """
    Given a list, this function returns a list with the numbers of the list sorted from largest to smallest.
    """
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst

# Test
print(reverse_sort_list([15, 3, 4948938]))
print(reverse_sort_list([15, 3, 4948938]))
</cell>
<text>
Exercise: Write a function that takes a list as input and returns a list with the numbers of the list sorted from smallest to largest.


</text>
<cell>
def sort_list_2(lst):
    """
    Given a list, this function returns a list with the numbers of the list sorted from smallest to largest.
    """
    sorted_lst = sorted(lst, key=lambda x: x)
    return sorted_lst

# Test
print(sort_list_2([15, 3, 4948938]))
print(sort_list_2([15, 3, 4948938]))
</cell>
<text>
Exercise: Write a function that takes a list as input and returns a list with the numbers of the list sorted from largest to smallest.


</text>
<cell>
def reverse_sort_list_2(lst):
    """
    Given a list, this function returns a list with the numbers of the list sorted from largest to smallest.
    """
    sorted_lst = sorted(lst, key=lambda x: x, reverse=True)
    return sorted_lst

# Test
print(reverse_sort_list_2([15, 3, 4948938]))
print(reverse_sort_list_2([