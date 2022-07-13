
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num

# Now let's try it out
for num in range(1, 101):
    print(fizzbuzz(num))
</cell>
<text>
The code above works, but it would be more efficient to write it as a list comprehension:


</text>
<cell>
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 17  (instead of the number),
        the number itself otherwise.
    """
    return [
        "FizzBuzz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else num
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else "Fizz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else "Buzz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else num
    ]

# Now let's try it out
for num in range(1, 101):
    print(fizzbuzz(num))
</cell>
<text>
The list comprehension above is more concise, but it's less efficient. Let's try it out on a larger number:


</text>
<cell>
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 17  (instead of the number),
        the number itself otherwise.
    """
    return [
        "FizzBuzz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else num
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else "Fizz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else "Buzz"
        if num % 15 == 0 and num % 3 == 0 and num % 5 == 0
        else num
        for num in range(1, 101)
    ]

# Now let's try it out
for num in range(1, 101):
    print(fizzbuzz(num))
</cell>
<text>
The list comprehension above is 