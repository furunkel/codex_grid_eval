
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x:x[2])[0]
</cell>
<cell>
extract_value(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with the first element repeated n times and the second element repeated m times.


</text>
<cell>
def repeat_elements(lst, n):
    """
    Given a list and a number, repeat the first element of the list n times.
    """
    return [lst[0]]*n+[lst[1]]*(m-n)
</cell>
<cell>
lst = [1,2,3]
repeat_elements(lst, 2)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with the first element repeated n times and the second element repeated m times. Assume that n is always greater than or equal to m.


</text>
<cell>
def repeat_elements(lst, n, m):
    """
    Given a list and a number, repeat the first element of the list n times.
    """
    return [lst[0]]*n+[lst[1]]*(m-n)
</cell>
<cell>
lst = [1,2,3]
repeat_elements(lst, 2, 4)
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with the first element repeated n times and the second element repeated m times. Assume that n is always less than or equal to m.


</text>
<cell>
def repeat_elements(lst, n, m):
    """
    Given a list and a number, repeat the first element of the list n times.
    """
    return [lst[0]]*n+[lst[1]]*(m-n)
</cell>
<cell>
lst = [1,2,3]
repeat_elements(lst, 2, 3)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with the first element repeated n times and the second element repeated m times. Assume that n is always less than or equal to m.


</text>
<cell>
def repeat_elements(lst, n, m):
    """
    Given a list and a number, repeat the first element of the list n times.
    """
    return [lst[0]]*n+[lst[1]]*(m-n)
</cell>
<cell>
lst = [1,2,3]
repeat_elements(lst, 2, 4)
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list with the first element repeated n times and the second element repeated m times. Assume that n is always less than or equal to m.


</text>
<cell>
def repeat_elements(lst, n, m):