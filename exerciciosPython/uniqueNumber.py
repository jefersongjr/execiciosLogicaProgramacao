#There is an array with some numbers. All numbers are equal except for one. Try to find it!


from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[-1][0]