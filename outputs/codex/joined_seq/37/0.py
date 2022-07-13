
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a plus and True otherwise.
    """
    return re.search(r'[a-z]+\+[a-z]+', text) is None

def main():
    print(joined_sequence('a+b+c'))
    print(joined_sequence('a+b+cd'))
    print(joined_sequence('a+b+c+d'))
    print(joined_sequence('a+b+c+d+e'))
    print(joined_sequence('a+b+c+d+e+f'))
    print(joined_sequence('a+b+c+d+e+f+g'))
    print(joined_sequence('a+b+c+d+e+f+g+h'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l+m'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l+m+n'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l+m+n+o'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q'))
    print(joined_sequence('a+b+c+d+e+f+g+h+i+j+k+l