
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[2])[1]
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the second value of the tuple with the largest twelfth value.


</text>
<cell>
def second_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[1])[2]
</cell>
<cell>
second_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the third value of the tuple with the largest twelfth value.


</text>
<cell>
def third_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[0])[2]
</cell>
<cell>
third_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the fourth value of the tuple with the largest twelfth value.


</text>
<cell>
def fourth_max(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[0])[3]
</cell>
<cell>
fourth_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the fifth value of the tuple with the largest twelfth value.


</text>
<cell>
def fifth_max(lst):
    """
    Given a list of tuples, write a function that returns the fifth value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[0])[4]
</cell>
<cell>
fifth_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the sixth value of the tuple with the largest twelfth value.


</text>
<cell>
def sixth_max(lst):
    """
    Given a list of tuples, write a function that returns the sixth value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda x:x[0])[5]
</cell>
<cell>
sixth_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that returns the seventh value of the tuple with the largest twelfth value.


</text>
<cell>
def seventh_