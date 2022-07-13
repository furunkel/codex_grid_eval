
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    
    return max(lst)[1]

#Test your solution by filling in the correct values
print(tuple_extract(lst))
</cell>
<text>
Question 3
Write a function that returns a list with the first n elements of a given list. 
For example, given the list [1,2,3,4,5], it should return [1,2].
Assume that the list has an even number of elements
Assume that n is positive (meaning you can assume that n is always positive)


</text>
<cell>
def first_n_elements(lst,n):
    """
    Given a list and a number n, return a list with the first n elements of the given list
    """
    
    return lst[:n]
</cell>
<cell>
#Test your solution by filling in the correct values
print(first_n_elements([1,2,3,4,5],2))
</cell>
<text>
Question 4
Write a function that returns a list with the last n elements of a given list. 
For example, given the list [1,2,3,4,5], it should return [3,4,5].
Assume that the list has an even number of elements
Assume that n is positive (meaning you can assume that n is always positive)


</text>
<cell>
def last_n_elements(lst,n):
    """
    Given a list and a number n, return a list with the last n elements of the given list
    """
    
    return lst[-n:]
</cell>
<cell>
#Test your solution by filling in the correct values
print(last_n_elements([1,2,3,4,5],2))
</cell>
<text>
Question 5
Write a function that returns a list with the n elements from the beginning of the given list. 
For example, given the list [1,2,3,4,5], it should return [1,2].
Assume that the list has an even number of elements
Assume that n is positive (meaning you can assume that n is always positive)


</text>
<cell>
def first_n_elements(lst,n):
    """
    Given a list and a number n, return a list with the first n elements of the given list
    """
    
    return lst[:n]
</cell>
<cell>
#Test your solution by filling in the correct values
print(first_n_elements([1,2,3,4,5],2))
</cell>
<text>
Question 6
Write a function that returns a list with the n elements from the end of the given list. 
For example, given the list [1,2,3,4,5], it should return [3,4,5].
Assume that the list has an even number of elements
Assume that n is positive (meaning you can assume that n is always positive)


</text>
<cell>
def last_n_elements(lst,n):
    """
    Given a list and a number n, return a list with the last n 