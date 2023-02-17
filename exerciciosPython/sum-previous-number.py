def countdown(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n + countdown(n - 1)


print(countdown(4))