rows_str, columns_str = input().split(" ")
rows = int(rows_str)
columns = int(columns_str)
text = "WELCOME"
pattern = ".|."
for i in range(1, rows - 1, 2):
    print((pattern * i).center(columns, "-"), )
print(text.center(columns, "-"))
for j in range(rows - 2, 0, -2):
    print((pattern * j).center(columns, "-"), )
