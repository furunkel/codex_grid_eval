

def sum_of_multiples(n):
    sum = 0
    for i in range(n):
        if i % 13 == 0 or i % 17 == 0:
            sum += i
    return sum

print(sum_of_multiples(197))