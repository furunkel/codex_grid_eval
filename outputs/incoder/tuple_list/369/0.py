
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst)[0]


# Test your function
print(some_func([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6)]))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given the list lst below, return a new list with all of the duplicates removed:

[1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8]

</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list without duplicates.
    """
    return list(set(lst))
</cell>
<cell>
# Test your function
print(remove_duplicates([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8]))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed and a dictionary that maps the numbers in the list to the number of times they appear.

For example, given the list lst below, return a new list with all of the duplicates removed and a dictionary that contains the original numbers as keys and their frequency as values:

[1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8] => {1: 4, 2: 2, 3: 1, 4: 2, 5: 1}

</text>
<cell>
def remove_duplicates_count_dict(lst):
    """
    Given a list of numbers, return a list without duplicates.
    """
    count = {}
    for x in lst:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return list(count.keys()), list(count.values())
</cell>
<cell>
# Test your function
print(remove_duplicates_count_dict([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8]))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed and a dictionary that maps the numbers in the list to the number of times they appear.

For example, given the list lst below, return a new list with all of the duplicates removed and a dictionary that contains the original numbers as keys and their frequency as values:

[1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8] => {1: 4, 2: 2, 3: 1, 4: 2, 5: 1}

</text>
<cell>
def remove_duplicates_count_dict_2(lst):
    """
    Given a list of numbers, return a list without duplicates.
    """
    count = {}
    for x in lst:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return list(count.keys()), list(count.values())
</cell>
<cell>
# Test your function
print(remove_duplicates_count_dict_2([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8]))
</cell>
<text>
Write a function that takes a list of numbers and a number, n, where n <= 