n = int(input())
total_length = len(format(n, 'b'))
for i in range(1, n + 1):
    print(
        f"{str(i).rjust(total_length)} {format(i, 'o').rjust(total_length)} {format(i, 'x').upper().rjust(total_length)} {format(i, 'b').rjust(total_length)}")
