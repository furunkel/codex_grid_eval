
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    
    # your code here
    
    return max(lst)
</cell>
<cell>
# test your code
lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(min_max(lst))
</cell>
<text>
Great job!

</text>
<text>
Dictionaries
Next up, we will cover dictionaries. These data structures are used extensively in Python, and they are extremely useful for storing data of any type.

Dictionaries are created with curly brackets, and each item is separated by a colon. Let's see how we can use them to record information!


</text>
<cell>
# Make a dictionary with seven items
info = {'name': 'Chris', 'age': 25, 'job': 'teacher'}
</cell>
<text>
Now let's look at a dictionary again:


</text>
<cell>
info
</cell>
<text>
It only has three items! How do we make it have seven items? That is where the dictionary comprehension comes in:


</text>
<cell>
info = {key1: val1, key2: val2, ..., keyN: valN}
</cell>
<text>
Now let's look at that dictionary again:


</text>
<cell>
info
</cell>
<text>
Much better, right?

Now you know how to make a dictionary in one line.

We will see this type of dictionary being used to collect information on students in a class. Let's do it!


</text>
<text>
Exercise
Write a dictionary that has the following items:

The names of the students
The ages of the students
A boolean that indicates if the student has passed the coursework
A list of the courses the student has taken

Then use that dictionary to make a new dictionary that has the following items:

The names of the students
The ages of the students
A boolean that indicates if the student has passed the coursework
A list of the courses the student has taken
A count of the number of times the student has passed the coursework
A list of the courses the student has taken, sorted by the number of courses the student has taken.

The dictionary should be created with at least seven items


</text>
<cell>
# Ex 3.1: Write a dictionary that has the following items:
# - The names of the students
# - The ages of the students
# - A boolean that indicates if the student has passed the coursework
# - A list of the courses the student has taken

# Put your code here
</cell>
<cell>
# Ex 3.2: 