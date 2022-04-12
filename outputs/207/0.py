

def multiples(n):
    return [x for x in range(n) if x % 5 == 0 or x % 7 == 0 or x % 9 == 0]

def product(n):
    return reduce(lambda x, y: x * y, multiples(n))

print product(600)