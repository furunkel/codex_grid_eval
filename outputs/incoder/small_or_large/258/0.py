
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 15 (and None if -100 <= n < 15).
    """
    if n < -100:
        return "large"
    elif n >= 15:
        return "house"
    else:
        return None


# Function to calculate average of n numbers
def average(n):
    """
        Given an integer n, return the average of all the numbers in the list.
    """
    sum = 0
    for num in n:
        sum += num
    return sum / len(n)


# Function to calculate standard deviation of n numbers
def standard_deviation(n):
    """
        Given an integer n, return the standard deviation of all the numbers in the list.
    """
    sum = 0
    for num in n:
        sum += (num - average(n))**2
    return math.sqrt(sum / len(n))


# Function to calculate median of n numbers
def median(n):
    """
        Given an integer n, return the median of all the numbers in the list.
    """
    sorted_list = sorted(n)
    length = len(sorted_list)
    if length % 2 == 0:
        return sorted_list[length//2]
    else:
        return (sorted_list[length//2] + sorted_list[length//2 - 1])/2


# Function to calculate mode of n numbers
def mode(n):
    """
        Given an integer n, return the mode of all the numbers in the list.
    """
    counts = {}
    for num in n:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_counts[0][0]


# Function to calculate quartiles of n numbers
def quartile(n):
    """
        Given an integer n, return the quartiles of all the numbers in the list.
    """
    sorted_list = sorted(n)
    length = len(sorted_list)
    if length % 2 == 0:
        return sorted_list[length//2]
    else:
        return (sorted_list[length//2] + sorted_list[length//2 - 1])/2


# Function to calculate quartiles of n numbers
def quartiles(n):
    """
        Given an integer n, return the quartiles of all the numbers in the list.
    """
    sorted_list = sorted(n)
    length = len(sorted_list)
    if length % 2 == 0:
        return sorted_list[length//2]
    else:
        return (sorted_list[length//2] + sorted_list[length//2 - 1])/2


# Function to calculate quartiles of n numbers
def quartiles(n):
    """
        Given an integer n, return the quartiles of all the numbers in the list.
    """
    sorted_list = sorted(n)
    length = len(sorted_list)
    if length % 2 == 0:
        return sorted_list[length//2]
    else:
        return (sorted_list[length//2] + sorted_list[length//2 - 1])/2