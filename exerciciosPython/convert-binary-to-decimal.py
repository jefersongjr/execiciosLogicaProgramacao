def binary_array_to_number(arr):
    converted_number = 0
    power = len(arr) - 1
    for number in arr:
        x = number * (2 ** power)
        converted_number += x
        power -= 1
    return converted_number