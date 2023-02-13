# dado determinado mês diga em qual quarto do ano ele está
def quarter_of(month):
    quarter_year = 0
    if month >= 1 and month <= 3:
        quarter_year = 1
    if month >= 4 and month <= 6:
        quarter_year = 2
    if month >= 7 and month <= 9:
        quarter_year = 3
    if month >= 10 and month <= 12:
        quarter_year = 4
    return quarter_year

#outra solução
# from math import ceil
# def quarter_of(month):
#     return ceil(month / 3)