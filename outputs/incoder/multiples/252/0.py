
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Great! Now you know how to sum all the multiples of 2 or 5 below 100. Can you do it in one line?


</text>
<cell>
# YOUR CODE HERE
</cell>
<text>
The sum of the multiples of 2 or 5 below 1000 is 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 + 22 + 24 + 26 + 28 + 30 + 32 + 34 + 36 + 38 + 40 + 42 +44 + 46 + 48 + 50 + 52 + 54 + 56 + 58 + 60 + 62 + 64 + 66 + 68 + 70 + 72 + 74 + 76 + 78 + 80 + 82 + 84 + 86 + 88 + 90 + 92 +94 + 96 + 98 + 100

</text>
<text>
Let's see a mathematical proof for this. The sum of the multiples of 2 or 5 below 1000 is 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 + 22 + 24 + 26 + 28 + 30 + 32 + 34 + 36 + 38 + 40 + 42 +44 + 46 + 48 + 50 + 52 + 54 + 56 + 58 + 60 + 62 + 64 + 66 + 68 + 70 + 72 + 74 + 76 + 78 + 80 + 82 + 84 + 86 + 88 + 90 + 92 +94 + 96 + 98 + 100
= (2 + 6 + 10 + 14 + 18)2 + (4 + 8 + 12 + 16 + 20)2 + (6 + 10 + 14 + 18 + 22)2 + (8 + 12 + 16 + 20 + 24)2 + (10 + 14 + 18 + 22 + 26)2 + (12 + 16 + 20 + 24 + 28)2 + (14 + 18 + 22 + 26 + 30)2 + (16 + 20 + 24 + 28 + 32)2 + (18 + 22 + 26 + 30 + 34)2 + (20 + 24 + 28 + 32 + 36)2 + (22 + 26 + 30 + 34 + 38)2 + (24 + 28 + 32 + 36 + 40)2 + (26 + 30 + 34 + 38 + 42)2 + (28 + 32 + 36 + 40 + 44)2 + (30 + 34 + 38 + 42 + 46)2 + (32 + 36 + 40 + 44 + 48)2 + (34 + 38 + 42 + 46 + 50)2 + (36 + 40 + 44 + 48 + 52)2 + (38 + 42 + 46 + 50 + 