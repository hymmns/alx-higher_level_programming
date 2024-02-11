#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            }

    if roman_string is None or type(roman_string) is not str:
        return None

    result = 0

    for each_char in roman_string:
        roman_value = roman_dict[each_char]

        if result > roman_value and result > 0:
            result = result + roman_value

        else:
            result = roman_value - result

    return result
