
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The sum of these multiples is 25.
    Return the sum of all the multiples of 2 or 5 below 500.
    """    
    
    sum = 0
    for i in range(1, 500):
        if i % 2 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 3
Use while True to write a loop that prints the integers from 1 to 50. After every iteration, print a newline and the value of i. Stop when the value of i is 50.

HINT: You can use a variable outside the loop to keep track of the current number.


</text>
<cell>
i = 1
while True:
    print(i)
    i += 1
    if i == 51:
        break
</cell>
<text>
Problem 4
Write a function that returns a list of all the even values from 1 to 30. After the loop, print a newline and the returned list.

HINT: You can use the range() function to help you create the list.


</text>
<cell>
def even_numbers():
    """
    Returns a list of all the even values from 1 to 30.
    """
    
    even_numbers = []
    for i in range(1, 31):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(even_numbers())
</cell>
<text>
Problem 5
Write a function that returns a list of all the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

Sample Output
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
Buzz
21
Fizz
23
24
FizzBuzz
Buzz
25
Fizz
27
28
Fizz
Buzz
Buzz
29
Fizz
Buzz
Buzz
Buzz
Buzz
31
Fizz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Buzz
Bu