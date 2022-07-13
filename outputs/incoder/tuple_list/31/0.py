
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[2])[0]

# Test case
print(tuple_extract(lst))
</cell>
<text>
Problem 7
Write a function that returns a list with the first n elements of the given list. 
If n is greater than the length of the list, return an empty list.
If n is less than or equal to the length of the list, return the same list with n elements removed.
If n is not given in the function call, use n=5.
Test your function with the following test cases:

lst = [1, 2, 3, 4, 5]
n = 5
Expected output: [1, 2, 3, 4]
lst = [1, 2, 3, 4, 5]
n = 3
Expected output: [1, 2]
lst = [1, 2, 3, 4, 5]
n = 4
Expected output: [1, 2, 3, 4]
lst = []
Expected output: []
lst = [1, 2, 3, 4, 5]
n = 6
Expected output: []
lst = [1, 2, 3, 4, 5]
n = 10
Expected output: [1, 2, 3, 4, 5]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 20
Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


</text>
<cell>
def first_n_elements(lst, n=5):
    """
    Given a list and a number n, return a list with the first n elements of the given list. 
    If n is greater than the length of the list, return an empty list.
    If n is less than or equal to the length of the list, return the same list with n elements removed.
    If n is not given in the function call, use n=5.
    """
    
    # Your code here
    
    return lst[:n]

# Test case
print(first_n_elements(lst))
print(first_n_elements(lst, 3))
print(first_n_elements(lst, 4))
print(first_n_elements(lst, 6))
print(first_n_elements(lst, 10))
print(first_n_elements(lst, 20))
</cell>
<text>
Problem 8
Write a function that returns a list with the first n elements of the given list. 
If n is greater than the length of the list, return an empty list.
If n is less than or equal to the length of the list, return the same list with n elements removed.
If n is not given in the function call, use n=5.
Test your function with the following test cases:

lst = [1, 2, 3, 4, 5]
n = 5
Expected output: [1, 2, 3, 4]
lst = [1, 2, 3, 4, 5]
n = 3
Expected output: [1, 2]
lst = [1, 2, 3, 4, 5]
n = 4
Expected output: [1, 2, 3, 4]
lst = []
Expected output: []
lst = [1, 2, 3, 4, 5]
n = 6
Expected output: []
lst = [1, 2, 3, 4, 5]
n = 10