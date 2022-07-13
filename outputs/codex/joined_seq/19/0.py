
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with six underscores and False otherwise.
    """
    return re.search(r'[a-z]+_+[a-z]+', text) is not None

def main():
    print(joined_sequence('abc_123_xyz'))
    print(joined_sequence('abc_xyz'))
    print(joined_sequence('abc_123_xyz_abc'))
    print(joined_sequence('abc_123_xyz_abc_123'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz_abc'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xyz_abc'))
    print(joined_sequence('abc_123_xyz_abc_123_xyz_abc_123_xyz_abc_123_xy