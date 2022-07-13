
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst)

# Test your function here
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 8
Write a function that takes a list of numbers and returns the sum of the numbers in the list. You may find the sum() function useful.


</text>
<cell>
def sum_func(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    return sum(lst)

# Test your function here
sum_func([3, 1, 2, 4])
</cell>
<text>
Problem 9
Write a function that returns a list of numbers, such that nums[0] + nums[1] + nums[2] + nums[3] is minimized.

HINT: You can use a greedy approach by starting with any three numbers (you can change these to whatever you want) and then repeatedly combining numbers in the list until you get a list that minimizes the sum of the list.


</text>
<cell>
def sum_func(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    lst = lst[:]
    lst.append(sum(lst))
    return lst

# Test your function here
sum_func([3, 1, 2, 4])
</cell>
<text>
Problem 10
You are provided with a list of words (you can assume that all the words are distinct), and a dictionary that relates each word to its length.

Write a function that returns a list of words in the same order as the provided list but where the words that are longer than the word with the smallest length come first.

For example, given the following input:

my_list = ['Hello', 'my', 'name', 'is', 'Bob']
my_dict = {'Hello': 5, 'my': 2, 'name': 6, 'is': 8, 'Bob': 9}
your function should return the following output:

['Bob', 9, 'Hello', 5, 'my', 2, 'name', 6]

</text>
<cell>
def first_word_func(my_list, my_dict):
    """
    Given a list of words and a dictionary of valid words, 
    return a list of words in the same order as the provided list
    but where the words that are longer than the word with the smallest length come first.
    """
    my_list = my_list[:]
    my_list.append(my_dict[min(my_dict)])
    return my_list

# Test your function here
my_list = ['Hello', 'my', 'name', 'is', 'Bob']
my_dict = {'Hello': 5, 'my': 2, 'name': 6, 'is': 8, 'Bob': 9}
first_word_func(my_list, my_dict)
</cell>
<text>
Great job!

</text>
<text>
Extra Credit
If you have extra time, try to solve the following problems with your functions. You will need at least three functions (although 