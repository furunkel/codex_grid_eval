
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[-1])
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_value(lst))
</cell>
<text>
If you only need the index, then use enumerate:


</text>
<cell>
def extract_index(lst):
    """
    Given a list of tuples, write a function that returns the index of the first tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(enumerate(lst), key=lambda x: x[1][-1])
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_index(lst))
</cell>
<text>
If you need to return the tuple with the largest eleventh value, then use enumerate:


</text>
<cell>
def extract_index(lst):
    """
    Given a list of tuples, write a function that returns the index of the first tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(enumerate(lst), key=lambda x: x[1][-1])[1]
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_index(lst))
</cell>
<text>
If you need to return the tuple with the largest eleventh value, then use enumerate:


</text>
<cell>
def extract_index(lst):
    """
    Given a list of tuples, write a function that returns the index of the first tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(enumerate(lst), key=lambda x: x[1][-1])[1]
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_index(lst))
</cell>
<text>
If you need to return the tuple with the largest eleventh value, then use enumerate:


</text>
<cell>
def extract_index(lst):
    """
    Given a list of tuples, write a function that returns the index of the first tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(enumerate(lst), key=lambda x: x[1][-1])[1]
</cell>
<cell>
# Test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_index(lst))
</