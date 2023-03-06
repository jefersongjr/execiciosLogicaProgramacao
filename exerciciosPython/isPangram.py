# A pangram is a sentence that contains every single letter 
# of the alphabet at least once. For example, the sentence "The quick 
#  fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True