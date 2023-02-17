def countdown(n):
    if n == 0:
        print("FIM!")
    else:
        print(n)
        countdown(n - 1) # caso recursivo


countdown(5)