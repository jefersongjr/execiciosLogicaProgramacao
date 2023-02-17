#Complete the solution so that it returns true if the first argument(string) 
# passed in ends with the 2nd argument (also a string). 

def solution(text, ending):
    x = len(ending)
    print(text[-x::])
    if ending in text[-x::]:
        return True
    return False