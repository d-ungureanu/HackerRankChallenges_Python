nr_of_lines = int(input())
input_list = []
for i in range(0, nr_of_lines):
    input_list.append([a, b] for a, b in input().split())
for entry in input_list:
    print(entry)