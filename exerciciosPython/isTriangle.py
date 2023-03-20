#Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built 
# with the sides of given length and false in any other case.


def is_triangle(a, b, c):
    if (abs(a - b) < c and
        abs(b - c) < a and
        abs(c - a) < b
       ):
        return True;   
    return False;