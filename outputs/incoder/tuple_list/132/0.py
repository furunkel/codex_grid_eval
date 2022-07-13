
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    lst = sorted(lst)
    
    return lst[-1][1]
</cell>
<cell>
extract_value(lst)
</cell>
<cell>
# Test your function
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(extract_value(lst))
</cell>
<text>
Dictionaries
Next you will create a dictionary that contains some cities and their states. It is guaranteed that the cities will be unique.

The dictionary will be in the form:

city_states = {'Miami': 'FL', 'Boston': 'MA', 'NYC': 'NY'}
Instructions:

Initialise the dictionary with city names as keys and state abbreviations as values.
Iterate over the dictionary to print out each city and its corresponding state.


</text>
<cell>
# Create a dictionary with city names as keys and state abbreviations as values
city_states = {'Miami': 'FL', 'Boston': 'MA', 'NYC': 'NY'}
</cell>
<cell>
# Write your function below!

def city_states(lst):
    """
    Given a list of tuples, write a function that returns a dictionary with the city names as keys and state abbreviations
    as values.
    """
    
    city_states = {}
    
    for city in lst:
        city_states[city[0]] = city[1]
        
    return city_states
</cell>
<cell>
# Test your function
lst = [('Boston', 'MA'), ('Miami', 'FL'), ('NYC', 'NY')]
print(city_states(lst))
</cell>
<text>
Great job!

</text>
<text>
Dictionaries are great for storing data where you know that the keys will be things and the values will be things you need to keep track of. In this case however, you know that the keys will be unique city names and the values will be unique abbreviations for the states. In this case, you don't need to use a dictionary because a tuple would suffice. Let's see how this would work.


</text>
<text>
Tuples
A tuple is similar to a list, but is immutable. Once created, a tuple can not be changed. In other words, once a tuple is created, it can not be changed.

The syntax for tuples is:

my_tuple = (1, 2, 3)
Instructions:

Create a tuple with three values equal to 1.
Print out the tuple to see what it looks like.
Change the value of the second element in the tuple to equal 3.
Print out the tuple to see what it looks like.


</text>
<cell>
# Create a tuple with 