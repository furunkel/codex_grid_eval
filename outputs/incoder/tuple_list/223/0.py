
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst)[2]
</cell>
<cell>
# Test your code
lst = [('Bob', 40), ('Alex', 50), ('Adam', 60)]
print(tuple_extract(lst))
</cell>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $1\leq i \leq n$. Your function should return a list of length $n+1$. You may use the following notation:

$x_0=2$

$x_1=$

$x_2=$

...

$x_n=$


</text>
<cell>
def squares(n):
    """
    Write a function that returns a list of numbers, such that $x_i=i^2$, for all $1\leq i \leq n$. Your function should return a list of length $n+1$. You may use the following notation:

    $x_0=2$

    $x_1=$

    $x_2=$

    ...

    $x_n=$
    """
    lst = []
    for i in range(n):
        lst.append(i**2)
    return lst
</cell>
<cell>
# Test your code
print(squares(10))
</cell>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $1\leq i \leq n$. Your function should return a list of length $n+1$. You may not use the following notation:

$x_0=2$

$x_1=$

$x_2=$

...

$x_n=$


</text>
<cell>
def squares(n):
    """
    Write a function that returns a list of numbers, such that $x_i=i^2$, for all $1\leq i \leq n$. Your function should return a list of length $n+1$. You may not use the following notation:

    $x_0=2$

    $x_1=$

    $x_2=$

    ...

    $x_n=$
    """
    lst = []
    for i in range(n):
        lst.append(i**2)
    return lst
</cell>
<cell>
# Test your code
print(squares(10))
</cell>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $1\leq i \leq n$. Your function should return a list of length $n+1$. You may not use the following notation:

$x_0=2$

$x_1=$

$x_2=$

...

$x_n=$


</text>
<cell>
def squares(n):
    """