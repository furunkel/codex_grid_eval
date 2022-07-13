
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "house" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return None


# In[13]:


def count_small_or_large(numbers):
    """
        Given a list of integers, return a list of tuples (n, small_or_large(n)).
    """
    small_or_large_list = []
    for n in numbers:
        small_or_large_list.append(small_or_large(n))
    return small_or_large_list


# In[14]:


def count_small_or_large_per_number(numbers):
    """
        Given a list of integers, return a dictionary of the form {n: (small_or_large(n), count_small_or_large(n))}.
    """
    small_or_large_per_number = {}
    for n in numbers:
        small_or_large_per_number[n] = (small_or_large(n), count_small_or_large(n))
    return small_or_large_per_number


# In[15]:


def count_small_or_large_per_number_and_percentage(numbers):
    """
        Given a list of integers, return a dictionary of the form {n: (small_or_large(n), count_small_or_large(n), percentage(n))}.
    """
    small_or_large_per_number_and_percentage = {}
    for n in numbers:
        small_or_large_per_number_and_percentage[n] = (small_or_large(n), count_small_or_large(n), percentage(n))
    return small_or_large_per_number_and_percentage


# In[16]:


def count_small_or_large_per_number_and_percentage_of_total(numbers):
    """
        Given a list of integers, return a dictionary of the form {n: (small_or_large(n), count_small_or_large(n), percentage(n), percentage_of_total(n))}.
    """
    small_or_large_per_number_and_percentage_of_total = {}
    for n in numbers:
        small_or_large_per_number_and_percentage_of_total[n] = (small_or_large(n), count_small_or_large(n), percentage(n), percentage_of_total(n))
    return small_or_large_per_number_and_percentage_of_total


# In[17]:


def count_small_or_large_per_number_and_percentage_of_total_and_percentage(numbers):
    """
        Given a list of integers, return a dictionary of the form {n: (small_or_large(n), count_small_or_large(n), percentage(n), percentage_of_total(n), percentage_of_total_and_percentage(n))}.
    """
    small_or_large_per_number_and_percentage_of_total_and_percentage = {}
    for n in numbers:
        small_or_large_per_number_and_percentage_of_total_and_percentage[n] = (small_or_large(n), count_small_or_large(n), percentage(n