#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to 
# contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    dict = {}
    sum = 0
    for i in text:
        if i.lower() not in dict:
            dict[i.lower()] = 1
        else:
            dict[i.lower()] += 1
    for key in dict:
        if dict[key] > 1:
            sum += 1
    return sum