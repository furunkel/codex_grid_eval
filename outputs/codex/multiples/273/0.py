
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 200.
    """    
    return reduce(lambda x, y: x * y, [x for x in range(1, 200) if x % 2 == 0 or x % 3 == 0 or x % 5 == 0])

def main():
    print multiples()

if __name__ == '__main__':
    main()