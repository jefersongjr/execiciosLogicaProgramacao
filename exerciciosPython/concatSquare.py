def square_digits(num):
    r = ''
    for x in str(num):
        y = int(x)
        r += str(y * y)
    return int(r)
        
