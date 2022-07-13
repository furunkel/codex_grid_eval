
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 3 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 3
Use while True to write a program that prints the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


</text>
<cell>
def fizzbuzz():
    """
    Print the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
    """
    
    sum = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            sum += i
    return sum

print(fizzbuzz())
</cell>
<text>
Problem 4
Write a program that prints the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


</text>
<cell>
def fizzbuzz():
    """
    Print the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
    """
    
    sum = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            sum += i
    return sum

print(fizzbuzz())
</cell>
<text>
Problem 5
Write a program that prints the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


</text>
<cell>
def fizzbuzz():
    """
    Print the integers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of 