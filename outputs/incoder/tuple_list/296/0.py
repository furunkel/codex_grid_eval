
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    # Your code here
    
    return max(lst)[1]
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the duplicates removed.

For example, given the list [1, 1, 2, 3, 4, 4, 4, 4, 4], the function should return [1, 2, 3, 4].


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list where there are no duplicate numbers.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
# Test your code
print(remove_duplicates([1, 1, 2, 3, 4, 4, 4, 4, 4]))
</cell>
<text>
Write a function that takes a list and returns a new list with all the duplicates removed where the number is replaced by the word 'Fizz'.

For example, given the list ['Fizz', 'Bob', 'Fizz', 'Bart', 'Fizz', 'Bob', 'Fizz'], the function should return ['Fizz', 'Bob', 'Bart', 'Fizz'].


</text>
<cell>
def remove_fizz(lst):
    """
    Given a list of words (strings), return a list where any word that contains the substring 'fizz' is replaced by the word 'fizz'.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
# Test your code
print(remove_fizz(['Fizz', 'Bob', 'Fizz', 'Bart', 'Fizz', 'Bob', 'Fizz']))
</cell>
<text>
Write a function that takes a list and returns a new list with all the duplicates removed where the number is replaced by the word 'Buzz'.

For example, given the list ['1', '2', '3', '4', '5', '6', '7', '8', '9'], the function should return ['1', '2', '3', '4', '5', '6', '7'].


</text>
<cell>
def remove_buzz(lst):
    """
    Given a list of numbers, return a list where any number that is a multiple of 3 is replaced by the word 'Buzz'.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
# Test your code
print(remove_buzz([1,2,3,4,5,6,7,8,9]))
</cell>
<text>
Write a function that takes a list and returns a new list with all the duplicates removed where the number is replaced by the word 'FizzBuzz'.

For example, given the list ['Fizz', 'Bob', 'Fizz', '