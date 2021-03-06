
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i + i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    3
    Then, the output should be:
    {1: 2, 2: 4, 3: 6}

    """
    
    dict = {}
    
    for i in range(1, n + 1):
        
        if i in dict:
            
            dict[i] = dict[i] + i
            
        else:
            
            dict[i] = i
            
    return dict
</cell>
<cell>
# test your code
print(generate_dict(4))
</cell>
<text>
Write a Python program to find the first non-repeating character in a given string. 
For example given the string 'bananas', the output should be 'n'.

</text>
<cell>
def first_non_repeated_char(string):
    
    dict = {}
    
    for i in string:
        
        if i in dict:
            
            dict[i] = dict[i] + 1
            
        else:
            
            dict[i] = 1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    