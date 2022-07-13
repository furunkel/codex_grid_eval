
def make_tuple(fkrjf4ifji4ofj, fekjfwoeifjwu5gfd):
    """
    Given two integers fkrjf4ifji4ofj and fekjfwoeifjwu5gfd, return a tuple where:
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    """
    
    third = fkrjf4ifji4ofj * fekjfwoeifjwu5gfd
    first = (fkrjf4ifji4ofj - fekjfwoeifjwu5gfd) 
    second = fkrjf4ifji4ofj + fekjfwoeifjwu5gfd
    
    return (third, first, second)
</cell>
<cell>
make_tuple(12, 3)
</cell>
<text>
Question 9
Write a Python function that takes a list as an argument and returns the sum of the elements of the list.


</text>
<cell>
def sum_of_list(lst):
    """
    Given a list lst, return the sum of the elements of the list.
    """
    
    sum = 0
    
    for element in lst:
        sum += element
    
    return sum
</cell>
<cell>
sum_of_list([1,2,3])
</cell>
<text>
Question 10
Write a Python function that takes a list as an argument and returns the product of the elements of the list.


</text>
<cell>
def product_of_list(lst):
    """
    Given a list lst, return the product of the elements of the list.
    """
    
    product = 1
    
    for element in lst:
        product *= element
    
    return product
</cell>
<cell>
product_of_list([1,2,3])
</cell>
<text>
Question 11
Write a Python function that takes a list as an argument and returns the product of the elements of the list divided by the sum of the elements of the list.


</text>
<cell>
def product_of_list_divided_by_sum(lst):
    """
    Given a list lst, return the product of the elements of the list divided by the sum of the elements of the list.
    """
    
    product = 1
    
    for element in lst:
        product *= element
    
    sum = sum_of_list(lst)
    
    return product / sum
</cell>
<cell>
product_of_list_divided_by_sum([1,2,3])
</cell>
<text>
Question 12
Write a Python function that takes a list as an argument and returns the product of the elements of the list divided by the sum of the elements of the list multiplied by the product of the elements of the list.


</text>
<cell>
def product_of_list_divided_by_sum_multiplied_by_product(lst):
    """
    Given a list lst, return the product of the elements of the list divided by the sum of the elements of the list multiplied by the product of the elements of the list.
    """
    
    product = 1
    
    for element in lst