

def sqrt_dict(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i**2
    return d

print(sqrt_dict(1))