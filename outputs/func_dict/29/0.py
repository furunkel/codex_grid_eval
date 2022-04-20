

def generate_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i**2
    return d

if __name__ == '__main__':
    n = int(input())
    print(generate_dict(n))