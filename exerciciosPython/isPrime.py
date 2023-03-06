#testa se um numero inteiro é primo

def divisors(integer):
    list = []
    for i in range(2, integer):
        if integer % i == 0:
            list.append(i)
    return str(integer) + ' is prime' if len(list) == 0 else list