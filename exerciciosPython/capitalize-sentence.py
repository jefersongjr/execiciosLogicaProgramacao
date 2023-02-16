#Colocando todas as primeiras letras das palavras em caixa alta;
def to_jaden_case(string):
    x = string.split(" ")
    y = ""
    for word in x:
     y += word.capitalize() +" " 
    return y.strip()

#   return ' '.join(word.capitalize() for word in string.split()) / outro jeito