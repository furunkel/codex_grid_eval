
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 7 or 9, we get 5, 7 and 9. The sum of these multiples is 21.
    Return the sum of all the multiples of 5, 7 or 9 below 600.
    """    
    return sum(i for i in range(1, 600) if i % 5 == 0 or i % 7 == 0 or i % 9 == 0)

def main():
    print(multiples())

if __name__ == "__main__":
    main()