results_list = []
number_of_tests = int(input("Number of tests: "))
for i in range(number_of_tests):
    length_set_a = int(input("length of set A:"))
    set_a = set(input("Elements of set A: ").split(" "))

    length_set_b = int(input("length of set B:"))
    set_b = set(input("Elements of set B: ").split(" "))

    results_list.append(set_a.issubset(set_b))

for entry in results_list:
    print(entry)

