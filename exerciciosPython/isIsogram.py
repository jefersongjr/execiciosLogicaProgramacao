#An isogram is a word that has no repeating letters,
#  consecutive or non-consecutive. Implement a function 
# that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.



def is_isogram(string):
    letters = {}
    for letter in string:
        if letter.lower() not in letters:
            letters[letter.lower()] = 1
        else:
            letters[letter.lower()] += 1
    x = 0
    for i in letters:
        if letters[i] > 1:
           x += 1
    return True if x == 0 else False

# def is_isogram(string):
    return len(string) == len(set(string.lower()))