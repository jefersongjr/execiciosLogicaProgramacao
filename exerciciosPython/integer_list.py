#create a function that takes a list of non-negative integers 
# and strings and returns a new list with the strings filtered out.

def filter_list(l):
    return [
        number 
        for number in l
        if type(number) == int and number >= 0
    ]