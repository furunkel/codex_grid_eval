
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 5, 3 or 2 below 197.
    """    
    return reduce(lambda x, y: x * y, set(range(2, 197, 2) + range(3, 197, 3) + range(5, 197, 5)))

def main():
    print multiples()

if __name__ == '__main__':
    main()