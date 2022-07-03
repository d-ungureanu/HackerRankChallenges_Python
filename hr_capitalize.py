import string


def solve(s):
    result_new = string.capwords(s, sep=" ")
    return result_new


if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
