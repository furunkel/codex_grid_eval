

def sqrt_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i**0.5
    return d

print(sqrt_dict(8))