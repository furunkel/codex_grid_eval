
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 124.
    """    
    
    multiples = []
    for n in range(124,150):
        if n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
            multiples.append(n)
    return multiples 

print(multiples())
</cell>
<text>
Great! Now you know how to check if a number is in a list, and how to get the product of a list. Next we will learn about for loops.


</text>
<text>
For Loops
The for loop will allow us to loop through each item in a list. For example,


</text>
<cell>
for number in [1, 2, 3]:
    print(number)
</cell>
<text>
This for loop will print out 1 then 2 and finally 3. We can also have an else statement that executes when the loop completes.


</text>
<cell>
for number in [1, 2, 3]:
    print(number)
else:
    print('All done!')
</cell>
<text>
We can also loop through tuples.


</text>
<cell>
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)
</cell>
<text>
For loops can also iterate through strings!


</text>
<cell>
words = 'red green blue'.split()
for word in words:
    print(word)
</cell>
<text>
We can also use while loops.


</text>
<cell>
i = 0
while i < 5:
    print(i)
    i = i + 1
</cell>
<text>
Functions
Functions are a way to package code that is reusable and can be called upon later. For example,


</text>
<cell>
def say_hello():
    print('hello')
</cell>
<text>
This function says hello. Let's see how we can call this function.


</text>
<cell>
say_hello()
</cell>
<text>
So what happens if we call say_hello() again? Notice it does not say hello anymore. This is because functions are objects and can be called upon with different parameters. Let's see how we can do this.


</text>
<cell>
say_hello()
</cell>
<text>
So what happens if we call say_hello() again? Notice it does not say hello anymore. This is because functions are objects and can be called upon with different parameters. Let's see how we can do this.


</text>
<cell>
say_hello()
</cell>
<text>
So what happens if we call say_hello() again? Notice it does not say hello anymore. This is because functions are objects and can be called upon with different parameters. Let's see how we can do this.


</text>
<cell>
say_hello()