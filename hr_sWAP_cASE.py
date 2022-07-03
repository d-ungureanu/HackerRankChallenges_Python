def swap_case(s):
    swapped_s = ""
    for character in s:
        if character.islower():
            swapped_s += character.capitalize()
        elif character.isupper():
            swapped_s += character.lower()
        else:
            swapped_s += character
    return swapped_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
