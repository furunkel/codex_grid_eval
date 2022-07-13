
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
#    print "Generating dictionary..."
    d = {}
    for i in range(1, n+1):
        d[i] = i
    return d

def generate_list(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    """
#    print "Generating list..."
    l = []
    for i in range(1, n+1):
        l.append(i)
    return l

def generate_dict_of_lists(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
#    print "Generating dictionary of lists..."
    d = {}
    for i in range(1, n+1):
        d[i] = i
    return d

def generate_list_of_dicts(n):
    """
    With a given integral number n, write a program to generate a list that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the list.
    
    """
#    print "Generating list of dictionaries..."
    l = []
    for i in range(1, n+1):
        l.append(i)
    return l

def generate_dict_of_lists_of_dicts(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
#    print "Generating dictionary of lists of dictionaries..."
    d = {}
    for i in range(1, n+1):
        d[i] = i
    return d

def generate_list_of_