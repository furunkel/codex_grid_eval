
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[-11][1]
</cell>
<cell>
extract_value(lst)
</cell>
<text>
Question 3
Write a function that takes a list of tuples and returns a list of tuples where the second element of the tuple is the sum of the first and third element of the tuple.


</text>
<cell>
def sum_of_first_and_third(lst):
    """
    Given a list of tuples, return a list where the second element of the tuple is the sum of the first and third element of the tuple.
    """
    
    lst = sorted(lst)
    
    return [(lst[i][0] + lst[i][1]) for i in range(len(lst))]
</cell>
<cell>
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
sum_of_first_and_third(lst)
</cell>
<text>
Question 4
Write a function that takes a list of tuples and returns a list of tuples where the second element of the tuple is the sum of the first and third element of the tuple.


</text>
<cell>
def sum_of_first_and_third(lst):
    """
    Given a list of tuples, return a list where the second element of the tuple is the sum of the first and third element of the tuple.
    """
    
    lst = sorted(lst)
    
    return [(lst[i][0] + lst[i][2]) for i in range(len(lst))]
</cell>
<cell>
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
sum_of_first_and_third(lst)
</cell>
<text>
Question 5
Write a function that takes a list of tuples and returns a list of tuples where the second element of the tuple is the sum of the first and third element of the tuple.


</text>
<cell>
def sum_of_first_and_third(lst):
    """
    Given a list of tuples, return a list where the second element of the tuple is the sum of the first and third element of the tuple.
    """
    
    lst = sorted(lst)
    
    return [(lst[i][0] + lst[i][2]) for i in range(len(lst))]
</cell>
<cell>
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
sum_of_first_and_third(lst)
</cell>
<text>
Question 6
Write a function that takes a list of tuples and returns a list of tuples where the second element of the tuple is the sum of the first and third element of the tuple.


</text>
<cell>
def sum_of_first_and_third(lst):
    """
    Given a list of tuples, return a list where the second element of the tuple is the sum of the first and third element of the tuple.
    """
    
    lst = sorted(lst