if __name__ == "__main__":
    number = input()
    reversed_number = number[::-1]
    new_number = ""
    for index, digit in enumerate(reversed_number):
        if (index + 1) % 3 != 0:
            new_number += digit
        else:
            new_number += digit + ","
    fixed_number = new_number.strip(",")[::-1]
    print(fixed_number)
