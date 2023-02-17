# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()