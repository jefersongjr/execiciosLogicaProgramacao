def disemvowel(string_):
    vogals = ["a", "e", "i", "o", "u"]
    phrase = ""
    for string in string_:
        if string.lower() not in vogals:
            phrase += string
    print(phrase)
    return phrase
