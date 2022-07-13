
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (9, 'd'), (8, 'e'), (7, 'f'), (6, 'g'), (5, 'h'), (4, 'i'), (3, 'j'), (2, 'k'), (1, 'l'), (9, 'm'), (8, 'n'), (7, 'o'), (6, 'p'), (5, 'q'), (4, 'r'), (3, 's'), (2, 't'), (1, 'u'), (9, 'v'), (8, 'w'), (7, 'x'), (6, 'y'), (5, 'z'), (4, 'a')]))
</cell>
<text>
Expected output
12

</text>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given [1,2,3,1,2,3], return [1,2,3].


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a new list containing all of the numbers in the list that occur more than once.
    """
    
    # Initialize an empty list to hold the unique numbers
    unique = []
    
    # Loop over every number in the list
    for num in lst:
        
        # If we haven't seen this number before, add it to the unique list
        if num not in unique:
            unique.append(num)
            
        # Otherwise, ignore the current number
        else:
            pass
    
    # Return the unique list
    return unique
</cell>
<cell>
print(remove_duplicates([1,2,3,1,2,3]))
</cell>
<text>
Expected output
[1, 2, 3]

</text>
<text>
Write a function that takes a list and returns a new list containing all of the numbers that occur more than twice.

For example, given [1,2,3,1,2,1,2], return [1,2,3].


</text>
<cell>
def remove_dupes(lst):
    """
    Given a list of numbers, return a new list containing all of the numbers in the list that occur more than twice.
    """
    
    # Initialize an empty list to hold the unique numbers
    unique = []
    
    # Loop over every number in the list
    for num in lst:
        
        # If we haven't seen this number before, add it to the unique list
        if num not in unique:
            unique.append(num)
            
        # Otherwise, ignore the current number
        else:
            pass
    
    # Return the unique list
    return unique
</cell>
<cell>
print(remove_dupes([1,2,3,1,2,1,2]))
</cell>
<text>
Expected output
[1, 2, 3]

</text>
<text>
Write a function that checks whether a number is "happy". An "happy" number is define