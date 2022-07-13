
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The product of these multiples is 5806080.
    Return the product of all the multiples of 2 or 9 below 197.
    """    
    
    multiples = []
    for n in range(2, int(math.sqrt(197)) + 1):
        if n % 2 == 0:
            multiples.append(n)
        if n % 9 == 0:
            multiples.append(n)
    return multiples[:]

# Now let's try it out!
print(multiples())
</cell>
<text>
Great! Now you know how to get the multiples of 2 and 9 using for loops. Next, let's write a function that will tell us how many of the numbers have 3 or 5 digits. You'll need to write a function like this so that it can take in any number given by the user and return the number of multiples of 3 or 5 below that number.


</text>
<cell>
def count_threes_or_fives(num):
    """
    Takes in a number from the user and returns the number of multiples of 3 or 5 below it.
    """
    
    count = 0
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            if num % 3 == 0:
                count += 1
            elif num % 5 == 0:
                count += 1
    return count

# Now let's see some examples:
print(count_threes_or_fives(19))
print(count_threes_or_fives(23))
print(count_threes_or_fives(25))
print(count_threes_or_fives(100))
print(count_threes_or_fives(1000))
</cell>
<text>
This is looking good. Now that we have this function, let's see how we might use while loops to get this done.

while Loops
The way you write a while loop is the same as a for loop, but there is a key difference. Let's see it in action using the while loop we created in a previous problem.

Write a while loop that prints the sum of all the odd numbers from 1 to 100. But while doing this, it also needs to keep track of the sum of all the even numbers from 1 to 100. Create a variable called total and assign it the value of the even number from 1 to 100.


</text>
<cell>
total = 0
while total < 100:
    if total % 2 == 0:
        total += 2
    else:
        total += 3
print(total)
</cell>
<text>
This works, but it looks very inefficient. Why don't we try to use a for loop?

For Loops
The for loop will allow us to iterate through each item in a list. Let's see how this works.

Write a for loop that prints all the odd numbers from 1 to 100. But instead of printing each number, it should also add the number to total. After doing so, also print out the sum of all the even numbers from 1 to 100.


</text>
<cell>
total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total 