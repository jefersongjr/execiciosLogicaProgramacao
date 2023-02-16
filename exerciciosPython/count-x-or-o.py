# função que conta se a quantidade de x equivale as de o;

def xo(s):
    x = 0
    o = 0
    for letter in s:
        if letter.lower() == "x":
            x += 1
        if letter.lower() == "o":
            o += 1 
        else:
            pass
    return x == o

    
# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')