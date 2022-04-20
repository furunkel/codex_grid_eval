

def sum_of_multiples(n):
    sum = 0
    for i in range(n):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
            sum += i
    return sum

print(sum_of_multiples(500))