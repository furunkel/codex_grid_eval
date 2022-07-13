
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[2])[2]
</cell>
<cell>
min_max(lst)
</cell>
<text>
Problem 7
Write a function that takes a list and a number as arguments and returns a list with the elements of the list that add up to that number.


</text>
<cell>
def sum_up(lst,n):
    """
    Given a list and a number, return a list with the elements of the list that add up to that number.
    """
    total = 0
    lst2 = []
    for x in lst:
        total += x[2]
        if total == n:
            lst2.append(x)
    return lst2
</cell>
<cell>
sum_up(lst,10)
</cell>
<text>
Problem 8
Write a function that takes a list and a number as arguments and returns a list with the elements of the list that multiply up to that number.


</text>
<cell>
def multiply_up(lst,n):
    """
    Given a list and a number, return a list with the elements of the list that multiply up to that number.
    """
    total = 0
    lst2 = []
    for x in lst:
        total += x[2]
        if total == n:
            lst2.append(x)
    return lst2
</cell>
<cell>
multiply_up(lst,10)
</cell>
<text>
Problem 9
Write a function that takes a list and a number as arguments and returns a list with the elements of the list that divide up to that number.


</text>
<cell>
def divide_up(lst,n):
    """
    Given a list and a number, return a list with the elements of the list that divide up to that number.
    """
    total = 0
    lst2 = []
    for x in lst:
        total += x[2]
        if total == n:
            lst2.append(x)
    return lst2
</cell>
<cell>
divide_up(lst,10)
</cell>
<text>
Problem 10
Write a function that takes a list and a number as arguments and returns a list with the elements of the list that multiply up to that number.


</text>
<cell>
def multiply_up(lst,n):
    """
    Given a list and a number, return a list with the elements of the list that multiply up to that number.
    """
    total = 0
    lst2 = []
    for x in lst:
        total += x[2]
        if total == n:
            lst2.append(x)
    return lst2
</cell>
<cell>
multiply_up(lst,10)
</cell>
<text>
Problem 11
Write a function that takes a list and a number as arguments and returns a list with the element