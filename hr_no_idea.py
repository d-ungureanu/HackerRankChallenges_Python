n, m = [int(entry) for entry in input().split()]
numbers_list = list(input().split())
set_a = set(input().split())
set_b = set(input().split())
happiness = sum((i in set_a) - (i in set_b) for i in numbers_list)
print(happiness)
