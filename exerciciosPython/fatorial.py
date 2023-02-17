def factorial(n):
    if n == 1:
        return 1
    else:
        x = n * factorial(n - 1)
        print(x)
        return x


print(factorial(10))