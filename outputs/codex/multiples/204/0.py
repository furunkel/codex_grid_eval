
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The sum of these multiples is 45.
    Return the sum of all the multiples of 5, 7 or 9 below 500.
    """    
    return sum(i for i in range(500) if i % 5 == 0 or i % 7 == 0 or i % 9 == 0)

def main():
    print(multiples())

if __name__ == "__main__":
    main()