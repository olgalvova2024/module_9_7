def is_prime(func):

    def wrapper(a, b, c):
        numbers = func(a, b, c)
        res_prime = 'Простое'
        if numbers == 1:
            res_prime = 'Не простое и не составное'
        else:
            for j in range((numbers - 2)):
                if numbers % (j + 2) == 0:
                    res_prime = 'Составное'
                    break
        print(res_prime)
        return numbers

    return wrapper
@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(-2, 3, 0)
print(result)

result = sum_three(-2, 3, 1)
print(result)

result = sum_three(2, 4, 6)
print(result)

