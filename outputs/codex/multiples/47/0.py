
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 2, 3 or 5 below 197.
    """    
    return reduce(lambda x, y: x * y, [x for x in range(1, 197) if x % 2 == 0 or x % 3 == 0 or x % 5 == 0])

def main():
    print multiples()

if __name__ == '__main__':
    main()